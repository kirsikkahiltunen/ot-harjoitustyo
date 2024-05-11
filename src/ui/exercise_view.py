from tkinter import Tk, ttk, constants
from repositories.card_repository import CardRepository
from cards import Card


class Exercise:
    """Luokka, joka vastaa tehtävä näkymästä.
    """
    def __init__(self, root, id, _show_exercise_list_view):
        """Luokan konstruktori, joka kutsuu luokkia CardRepository ja Card sekä 
        hakee näytettävän kysymyksen ja luo tehtävä näkymän.
        Args:
            root: Tkinter:in juuri
            id (int): tehtävän id
            _show_exercise_list_view: arvo, jota kutsutaan, kun siirrytään tehtävälista näkymään.
        """
        self._root = root
        self._frame = None
        self._exercise_id = id
        self.question = None
        self._show_exercise_list_view = _show_exercise_list_view

        self.card_repo = CardRepository()
        self.card = Card()
        self.question = self.get_question()
        self.exercise_frame()

    def pack(self):
        """Näyttää exercise_frame()-funktion määrittämän näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näytetyn näkymän.
        """
        self._frame.destroy()

    def get_question(self):
        """Hakee näytettävän kysymyksen.

        Returns:
            question: Tehtävän kysymys merkkijonona.
        """
        question = self.card_repo.get_question(self._exercise_id)
        return question

    def exercise_frame(self, message=None):
        """Määrittää tehtävä näkymän komponentit ja asettelun.

        Args:
            message: Käyttäjälle näytettävä viesti. Defaults to None.
        """
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid(row=0, column=0)
        question_text = ttk.Label(master=self._frame,
                                  text=self.question, font=("Arial", 16))
        question_text.grid(row=2, column=1, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        if message:
            message_label = ttk.Label(master=self._frame,
                                      text=message, font=("Arial", 12))
            message_label.grid(row=3, column=1, columnspan=2,
                               sticky=constants.W, padx=5, pady=5)
            correct_answer_text = self.card_repo.get_correct_answer_text(
                self._exercise_id)
            correct_answer = ttk.Label(master=self._frame,
                                       text=correct_answer_text, font=("Arial", 12))
            correct_answer.grid(row=4, column=1, columnspan=2,
                                sticky=constants.W, padx=5, pady=5)
            return_button = ttk.Button(
                master=self._frame, text="Palaa tehtävävalikkoon", command=self.show_exercise_list_view)
            return_button.grid(row=6, column=2, columnspan=1, sticky=(
                constants.E, constants.W), padx=5, pady=5)
        else:
            self._answer_entry = ttk.Entry(master=self._frame)
            self._answer_entry.grid(row=6, column=1, sticky=(
                constants.E, constants.W), padx=5, pady=5)
            submit = ttk.Button(master=self._frame,
                                text="Tarkista", command=self._check_answer)
            submit.grid(row=6, column=2, columnspan=1, sticky=(
                constants.E, constants.W), padx=5, pady=5)
            return_button = ttk.Button(
                master=self._frame, text="Palaa tehtävävalikkoon", command=self.show_exercise_list_view)
            return_button.grid(row=7, column=1, columnspan=1, sticky=(
                constants.E, constants.W), padx=5, pady=5)

    def _check_answer(self):
        """Tarkistaa onko käyttäjän antama vastaus oikein.
        Mikäli vastaus on väärin, lisätään se review_exercises tauluun. 
        """
        answer = self._answer_entry.get()
        is_correct = self.card_repo.solve_exercise(self._exercise_id, answer)
        if is_correct == True:
            self.destroy()
            message = "Hienoa, vastauksesi on oikein"
            self.exercise_frame(message)
            self.pack()
        else:
            self.destroy()
            self.card_repo.save_to_review_exercises(self._exercise_id)
            message = "Vastaus on väärin, tehtävä tallennettu kertaustehtäviin"
            self.exercise_frame(message)
            self.pack()

    def show_exercise_list_view(self):
        """Vie käyttäjän takaisin tehtävälista näkymään.
        """
        self._show_exercise_list_view()
