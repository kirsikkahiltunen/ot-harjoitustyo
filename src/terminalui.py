from cards import Card


class TerminalUI:
    def __init__(self):
        self.category_int = None
        self.card = None
        self.answer = None
        self.help = None
        self.cardcount = 0
        self.correct_count = 0

    def start_app(self):
        print("Hei! Tervetuloa käyttämään fysiikankertaus sovellusta")
        self.select()

    def select(self):
        print("Valitse, minkä aihealueen tehtäviä haluat harjoitella:\npaine=1\nliike-energia=2")
        print("0 lopettaa")
        category = input("Anna harjoiteltavan kategorian numero:")
        if category == "0":
            self.end_session()
        self.category_int = int(category)
        self.card = Card(self.category_int)
        self.print_question()

    def print_question(self):
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
        self.answer = input(
            "Anna tähän tehtävän vastaus kahden desimaalin tarkkuudella: ")
        self.calculate_correct_answer()

    def ask_for_help(self):
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
        percent = (self.correct_count/self.cardcount)*100
        print("Kiitos sovelluksen käytöstä!")
        print(
            f"Vastasit yhteensä {self.cardcount} tehtävään, joista {self.correct_count} eli {percent:.2f}% sait ensimmäisellä yrityksellä oikein.")


if __name__ == "__main__":
    app = TerminalUI()
    app.start_app()
