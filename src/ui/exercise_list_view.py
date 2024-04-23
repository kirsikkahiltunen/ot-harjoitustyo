from tkinter import Tk, ttk, constants


class ExerciseList:

    def __init__(self, root):
        self._root = root
        self._frame = None

        self.exercise_list_frame()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def exercise_list_frame(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="Tervetuloa sovellukseen!", font=("Arial", 30))
        label.grid(row=0, column=0, columnspan=2,
                   sticky=constants.W, padx=5, pady=5)
