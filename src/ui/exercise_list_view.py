from tkinter import Tk, ttk, constants
from repositories.card_repository import CardRepository
from repositories.user_repository import UserRepository


class ExerciseList:
    """Luokka, joka vastaa tehtäväkategoria listan näyttämisestä.
    """
    def __init__(self, root, _show_exercise_view, _show_login):
        """Luokan konstruktori, 
         joka kutsuu luokkia CardRepository ja UserRepository sekä 
         luo tehtäväkategorialista näkymän.

        Args:
            root: Tkinter:in juuri
            _show_exercise_view: arvo, jota kutsutaan, kun siirrytään tehtävä näkymään.
            _show_login: arvo, jota kutsutaan, kun käyttäjä kirjautuu ulos,
            näyttää kirjautumisnäkymän.
        """
        self._root = root
        self._frame = None
        self._show_exercise_view = _show_exercise_view
        self._show_login = _show_login
        self.card_repo = CardRepository()
        self.user_repo = UserRepository()
        self.exercise_list_frame()

    def pack(self):
        """Näyttää exercise_list_frame()-funktion määrittämän näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa viimeisimmän näkymän.
        """
        self._frame.destroy()

    def get_exercise_list(self):
        """Kutsuu luokan CardRepository funktiota list_all,
        jotta exercises taulun kaikki tehtävät saadaan haettua.

        Returns:
           exercise_list: Exercises -tietokantataulun rivit
        """
        exercise_list = self.card_repo.list_all()
        return exercise_list

    def get_card_category(self, category):
        """Etsii tehtävän kategoria numeron avulla 
        tekstimuotoisen kategorian nimen ja palauttaa sen.

        Args:
            category (int): kategoriaa vastaava numero

        Returns:
            card_category (str): palauttaa merkkijonona kategorian nimen.
        """
        card_category = self.card_repo.find_category(category)
        return card_category

    def exercise_list_frame(self):
        """Määrittää tehtävälista näkymän komponentit ja asettelun.
        """
        i = 3
        exercise_list = self.get_exercise_list()
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="Tervetuloa sovellukseen!", font=("Arial", 20))
        label.grid(row=0, column=1, columnspan=2,
                   sticky=constants.W, padx=5, pady=5)
        logout_button = ttk.Button(master=self._frame, text="Kirjaudu ulos",
                                   command=self._logout)
        logout_button.grid(row=1, column=1, columnspan=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        label_categories = ttk.Label(master=self._frame,
                                     text="Voit harjoitella seuraavia tehtävä kategorioita:", font=("Arial", 16))
        label_categories.grid(row=2, column=1, columnspan=2,
                              sticky=constants.W, padx=5, pady=5)
        for exercise in exercise_list:
            category = self.get_card_category(exercise[1])
            label_exercise = ttk.Label(master=self._frame,
                                       text=category, font=("Arial", 13))
            label_exercise.grid(row=i, column=1, columnspan=2,
                                sticky=constants.W, padx=5, pady=5)
            exercise_id = int(exercise[0])
            button = ttk.Button(master=self._frame, text="Tee tehtävä",
                                command=lambda exercise_id=exercise_id: self._exercise_selection(exercise_id))
            button.grid(row=i+1, column=1, columnspan=1, sticky=(
                constants.E, constants.W), padx=5, pady=5)
            i += 2

    def _exercise_selection(self, exercise_id):
        """Käsittelee käyttäjän tekemän tehtävävalinnan.

        Args:
            exercise_id (int): tehtävän id
        """
        self.viewnext(exercise_id)

    def viewnext(self, exercise_id):
        """Vie käyttäjän valitun tehtävän näkymään.

        Args:
            exercise_id (int): tehtävän id
        """
        self._show_exercise_view(exercise_id)

    def _logout(self):
        """Käsittelee käyttäjän ulos kirjautumisen.
        """
        self.user_repo.logout()
        self.viewlogin()

    def viewlogin(self):
        """Vie käyttäjän takaisin kirjautumisnäkymään.
        """
        self._show_login()
