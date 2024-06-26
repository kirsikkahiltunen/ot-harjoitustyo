from ui.login_view import LoginView
from ui.exercise_list_view import ExerciseList
from ui.create_user_view import CreateUserView
from ui.exercise_view import Exercise


class UI:
    """Sovelluksen graafisesta käyttöliittymästä vastaava luokka
    """

    def __init__(self, root):
        """Luokan konstruktori.Luo uuden juuren.

        Args:
            root: Tkinter:in juuri.
            self._current_view: määrittää nykyisen näkymän.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Aloittaa käyttöliittymän suorituksen.
        """
        self._show_login()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän, kun siirrytään seuraavaan näkymään.
        """
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_login(self):
        """Näyttää käyttäjälle kirjautumisnäkymän.
        """
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_create_user,
            self._show_exercise_list_view
        )
        self._current_view.pack()

    def _show_create_user(self):
        """Näyttää käyttäjälle näkymän, jossa käyttäjä voi luoda uuden käyttäjätunnuksen ja salasanan.
        """
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._show_login
        )
        self._current_view.pack()

    def _show_exercise_list_view(self):
        """Näyttää näkymän, jossa on listattuna exercises -taulun tehtäväkategoriat.
        """
        self._hide_current_view()

        self._current_view = ExerciseList(
            self._root,
            self._show_exercise_view,
            self._show_login
        )
        self._current_view.pack()

    def _show_exercise_view(self, id):
        """Näyttää käyttäjälle, tämän valitseman tehtävän.

        Args:
            id (int): näytettävän tehtävän id
        """
        self._hide_current_view()

        self._current_view = Exercise(
            self._root,
            id,
            self._show_exercise_list_view
        )
        self._current_view.pack()
