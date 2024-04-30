from tkinter import Tk, ttk, constants
from repositories.card_repository import CardRepository


class ExerciseList:

    def __init__(self, root):
        self._root = root
        self._frame = None

        self.card_repo = CardRepository()
        self.exercise_list_frame()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def get_exercise_list(self):
        exercise_list = self.card_repo.list_all()
        return exercise_list

    def exercise_list_frame(self):
        i = 2
        exercise_list = self.get_exercise_list()
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="Tervetuloa sovellukseen!", font=("Arial", 20))
        label.grid(row=0, column=1, columnspan=2,
                   sticky=constants.W, padx=5, pady=5)
        label_categories = ttk.Label(master=self._frame,
                                     text="Voit harjoitella seuraavia tehtävä kategorioita:", font=("Arial", 16))
        label_categories.grid(row=1, column=1, columnspan=2,
                              sticky=constants.W, padx=5, pady=5)
        for exercise in exercise_list:
            if exercise[0] == 1:
                label_exercise = ttk.Label(master=self._frame,
                                           text="Paine", font=("Arial", 13))
                label_exercise.grid(row=i, column=1, columnspan=2,
                                    sticky=constants.W, padx=5, pady=5)
            elif exercise[0] == 2:
                label_exercise = ttk.Label(master=self._frame,
                                           text="Liike-energia", font=("Arial", 13))
                label_exercise.grid(row=i, column=1, columnspan=2,
                                    sticky=constants.W, padx=5, pady=5)
            i += 1
