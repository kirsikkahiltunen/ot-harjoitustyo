from tkinter import Tk, ttk, constants


class CreateUserView:
    def __init__(self, root, _show_login):

        self._root = root
        self._frame = None
        self._show_login = _show_login
        self._username_entry = None
        self._password_entry = None
        self._password_again_entry = None

        self.create_user_frame()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def create_user_frame(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Luo käyttäjänimi ja salasana")

        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_again_label = ttk.Label(
            master=self._frame, text="Salasana uudestaan")
        self._password_again_entry = ttk.Entry(master=self._frame, show="*")

        button = ttk.Button(master=self._frame, text="Rekisteröidy",
                            command=self._create_user_handler)

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)

        username_label.grid(row=1, column=0, padx=5, pady=5)

        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=2, column=0, padx=5, pady=5)

        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button.grid(row=4, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_again_label.grid(row=3, column=0, padx=10, pady=10)

        self._password_again_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        password_again = self._password_again_entry.get()

        if len(username) > 0:
            if len(password) > 0:
                if len(password_again) > 0:
                    self._show_login()

        else:
            self._show_error("Kaikki kentät on täytettävä")