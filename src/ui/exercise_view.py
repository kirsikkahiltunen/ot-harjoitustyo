from tkinter import Tk, ttk, constants
from repositories.card_repository import CardRepository


class Exercise:

    def __init__(self, root, id):
        self._root = root
        self._frame = None
        self._exercise_selection = id

        self.card_repo = CardRepository()
        self.exercise_frame()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def get_question(self):
        question = self.card_repo.get_question(self._exercise_selection)
        return question

    def exercise_frame(self):
        self._frame = ttk.Frame(master=self._root)
        question=self.get_question()
        question_text = ttk.Label(master=self._frame,
                          text= question, font=("Arial", 16))
        question_text.grid(row=2, column=1, columnspan=2,
                   sticky=constants.W, padx=5, pady=5)