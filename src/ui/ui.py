from ui.login_view import LoginView
from ui.exercise_list_view import ExerciseList
from ui.create_user_view import CreateUserView


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_login(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_create_user,
            self._show_exercise_list_view
        )

        self._current_view.pack()

    def _show_create_user(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._show_login
        )

        self._current_view.pack()

    def _show_exercise_list_view(self):
        self._hide_current_view()

        self._current_view = ExerciseList(
            self._root,
            # self._show_index_view,
            # self._show_login
        )

        self._current_view.pack()
