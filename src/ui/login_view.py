from tkinter import Tk, ttk, constants
from repositories.user_repository import UserRepository


class LoginView:
    """Luokka, joka vastaa sisäänkirjautumisnäkymästä.
    """
    def __init__(self, root, _show_create_user, _show_exercise_list_view):
        """Luokan konstruktori, jossa kutsutaan UserRepository:a sekä luodaan kirjautumisnäkymä.

        Args:
            root: Tkinter:in juuri
            _show_create_user: arvo, jota kutsutaan, kun siirrytään käyttäjätunnuksen luonti näkymään.
            _show_exercise_list_view: arvo, jota kutsutaan, kun siirrytään tehtävälista näkymään.
        """
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._frame = None
        self._show_exercise_list_view = _show_exercise_list_view
        self._show_create_user_view = _show_create_user

        self.user_repo = UserRepository()
        self.login_frame()

    def pack(self):
        """Näyttää login_frame()-funktion määrittämän näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa viimeisimmän näkymän.
        """
        self._frame.destroy()

    def login_frame(self, message=None):
        """Määrittää kirjautumissivun komponentit ja asettelun.

        Args:
            message: Käyttäjälle näytettävä viesti. Defaults to None.
        """

        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Kirjaudu sovellukseen")

        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        button = ttk.Button(master=self._frame, text="Kirjaudu",
                            command=self._login_handler)

        create_user_label = ttk.Label(
            master=self._frame, text="Etkö ole vielä käyttäjä, luo tunnus tästä:")

        button_register = ttk.Button(master=self._frame, text="Rekisteröidy käyttäjäksi",
                                     command=self._create_new_handler)

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)

        username_label.grid(row=1, column=0, padx=5, pady=5)

        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=2, column=0, padx=5, pady=5)

        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button.grid(row=3, column=1, columnspan=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        create_user_label.grid(row=4, column=0, padx=10, pady=10)

        button_register.grid(row=4, column=1, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

        if message:
            message_label = ttk.Label(
                master=self._frame, text=message)
            message_label.grid(row=5, column=0, padx=10, pady=10)

    def _login_handler(self):
        """Käsittelee sisäänkirjautumisen.
        """
        self._username = self._username_entry.get()
        self._password = self._password_entry.get()

        if self.user_repo.login(self._username, self._password):
            self.viewnext()
        else:
            self.destroy()
            message = "Käyttäjätunnus tai salasana väärin"
            self.login_frame(message)
            self.pack()

    def viewnext(self):
        """Vie käyttäjän tehtävälistaus näkymään.
        """
        self._show_exercise_list_view()

    def _create_new_handler(self):
        """Vie käyttäjän uuden tunnuksen luonti näkymään.
        """
        self._show_create_user_view()
