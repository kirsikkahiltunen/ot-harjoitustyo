from tkinter import Tk, ttk, constants
from repositories.card_repository import CardRepository


class ExerciseList:

    def __init__(self, root, _show_exercise_view):
        self._root = root
        self._frame = None
        self._show_exercise_view = _show_exercise_view
        self.card_repo = CardRepository()
        self.exercise_list_frame()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def get_exercise_list(self):
        exercise_list = self.card_repo.list_all()
        return exercise_list
    
    def get_card_category(self, category):
        card_category = self.card_repo.find_category(category)
        return card_category

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
            category=self.get_card_category(exercise[1])
            label_exercise = ttk.Label(master=self._frame,
                                        text=category, font=("Arial", 13))
            label_exercise.grid(row=i, column=1, columnspan=2,
                                sticky=constants.W, padx=5, pady=5)
            id=int(exercise[0])
            button = ttk.Button(master=self._frame, text="Tee tehtävä",
                            command= lambda:self._exercise_selection(1))
            button.grid(row=i+1, column=1, columnspan=2, sticky=(
                constants.E, constants.W), padx=5, pady=5)
            print(id)
            i += 2


    def _exercise_selection(self, id):
        self.viewnext(id)

    def viewnext(self, id):
        self._show_exercise_view(id)
