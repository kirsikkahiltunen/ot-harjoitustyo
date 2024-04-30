from cards import Card
from repositories.user_repository import UserRepository


class TerminalUI:
    """Luokka, jonka avulla käytetään sovelluksen tekstipohjaista käyttöliittymää
    """

    def __init__(self):
        """Luokan konstruktori, joka kutsuu luokkaa UserRepository ja
          tallentaa sen muuttujaan sekä alustaa luokan muut muuttujat.
        """
        self.category_int = None
        self.card = None
        self.answer = None
        self.help = None
        self.cardcount = 0
        self.correct_count = 0

        self.user_repo = UserRepository()

    def start_app(self):
        """Aloittaa sovelluksen suorittamisen ja näyttää aloitus valikon. 
        Vie käyttäjän kirjautumis tai rekisteröitymis näkymään tehdyn valinnan mukaan.
        """
        print("Hei! Tervetuloa käyttämään fysiikankertaus sovellusta")
        print("Valitse mitä haluat tehdä")
        print("1 kirjaudu sisään")
        print("2 rekisteröidy käyttäjäksi")
        choice = input("Anna valinta:")
        if choice == "1":
            self.login()
        elif choice == "2":
            self.register()
        else:
            print("Virheellinen valinta")
            self.start_app()
        self.select()

    def login(self):
        """Kirjautumisnäkymä. Mikäli salasana ja käyttäjätunnus ovat oikein kutsutaan päävalikkonäkymää.
        """
        username = input("Anna käyttäjätunnus: ")
        password = input("Anna salasana: ")
        if self.user_repo.login(username, password):
            self.select()
        else:
            self.login()

    def register(self):
        """Rekisteröitymisnäkymä, jossa voi luoda uuden käyttäjätunnuksen ja salasanan.
           Mikäli käyttäjätunnusta ei ole vielä varattu, kättäjätunnus ja salasana tallennetaan "users" tietokantaan ja 
           käyttäjä viedään päävalikko näkymään.
           Jos käyttäjätunnus on jo käytössä, tulostetaan virheilmoitus ja kutsutaan uudestaan tätä samaa rekisteröitymisnäkymää.
        """
        username = input("Anna käyttäjätunnus: ")
        password = input("Anna salasana: ")
        if len(username) > 0:
            if len(password) > 0:
                try:
                    if self.user_repo.create_user(username, password):
                        self.select()
                    else:
                        print(
                            f"Käyttäjätunnus {username} on varattu, käytä toista käyttäjätunnusta")
                        self.register()
                except Exception as e:
                    print("Error:", e)

    def select(self):
        """Päävalikko näkymä, jossa käyttäjä valitsee minkä aihealueen tehtäviä hän haluaa opiskella tai lopettaa sovelluksen suorittamisen.
        """
        print("Valitse, minkä aihealueen tehtäviä haluat harjoitella:\npaine=1\nliike-energia=2")
        print("0 lopettaa")
        category = input("Anna harjoiteltavan kategorian numero:")
        if category == "0":
            self.end_session()
        self.category_int = int(category)
        self.card = Card(self.category_int)
        self.print_question()

    def print_question(self):
        """Kutsuu Card luokan funktiota, joka generoi tehtävän muuttujat ja tulostaa tämän jälkeen kysymyksen.
        """
        if self.category_int == 1:
            self.card.generate_variables()

            force = self.card.force
            area = self.card.area

            print(
                f"Emma seisoo yhdellä jalalla, hänen kengän pintaala on {area} neliömetriä ja hänen kengän alueelle kohdistuva voima on {force} newtonia, laske kuinka suuren paineen Emma aiheuttaa maahan.")
            self.cardcount += 1
            self.get_answer_from_user()

        elif self.category_int == 2:
            self.card.generate_variables()

            mass = self.card.mass
            velocity = self.card.velocity

            print(
                f"Laske ajoneuvon liike-energia kun sen nopeus on {velocity} metriä sekunnissa ja massa {mass} kilogrammaa")
            self.cardcount += 1
            self.get_answer_from_user()

    def get_answer_from_user(self):
        """Pyytää käyttäjältä tämän vastauksen.
        """
        self.answer = input(
            "Anna tähän tehtävän vastaus kahden desimaalin tarkkuudella: ")
        self.calculate_correct_answer()

    def ask_for_help(self):
        """Kysyy tarvitseeko käyttäjä vihjeen.
           Mikäli käyttäjä valitsee haluavansa vihjeen, tulostetaan tehtävän ratkaisua helpottava vihje.
           Käyttäjä saa kokeilla vastata tehtävään uudestaan.
        """
        self.help = input(
            "Oletko umpikujassa? Mikäli haluat vihjeen tehtävän ratkaisuun valitse 'Y', muussa tapauksessa valitse 'N', '0' lopettaa: ")
        if self.help == "Y":
            print(self.card.give_hint())
            self.get_answer_from_user()
        elif self.help == "N":
            print("Valitsit, ettet halua vihjettä. Voit nyt yrittää tehtävää uudestaan.")
            self.get_answer_from_user()
        elif self.help == "0":
            self.end_session()

    def calculate_correct_answer(self):
        correct_answer = self.card.solve()
        if self.answer == correct_answer:
            print("Hienoa, vastaus on oikein!")
            self.correct_count += 1
            solution = self.card.show_solution()
            print(solution)
            print("\n\n")

            self.select()

        else:
            print("Vastaus on virheellinen")
            self.ask_for_help()

    def end_session(self):
        print("Kiitos sovelluksen käytöstä!")
        if self.correct_count > 0 and self.cardcount > 0:
            percent = (self.correct_count/self.cardcount)*100
            print(
                f"Vastasit yhteensä {self.cardcount} tehtävään, joista {self.correct_count} eli {percent:.2f}% sait ensimmäisellä yrityksellä oikein.")


if __name__ == "__main__":
    app = TerminalUI()
    app.start_app()
