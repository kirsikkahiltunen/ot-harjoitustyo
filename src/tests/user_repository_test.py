import unittest
from repositories.user_repository import UserRepository


class TestUserRepo(unittest.TestCase):
    def setUp(self):
        self.user_repo = UserRepository()
        self.user_repo.delete_all_users()

    def test_create_user_adds_new_user_to_users(self):
        self.user_repo.create_user("Testi", "Testi123")
        users = self.user_repo.find_user_by_username("Testi")
        self.assertNotEqual(users, None)

    def test_list_all_finds_all_rows(self):
        self.user_repo.create_user("Testi", "Testi123")
        self.user_repo.create_user("Testi2", "Testi321")
        users = self.user_repo.list_all()
        self.assertEqual(len(users), 2)

    def test_login_works_correctly_with_right_username_and_password(self):
        self.user_repo.create_user("Testi", "Testi123")
        login = self.user_repo.login("Testi", "Testi123")
        self.assertEqual(login, True)

    def test_same_username_can_not_be_created_twise(self):
        self.user_repo.create_user("Testi", "Testi123")
        create_user = self.user_repo.create_user("Testi", "Testi123")
        self.assertEqual(create_user, False)

    def test_if_username_is_incorrect_login_fails(self):
        self.user_repo.create_user("Testi", "Testi123")
        login = self.user_repo.login("Test1", "Testi123")
        self.assertEqual(login, False)

    def test_if_password_is_incorrect_login_fails(self):
        self.user_repo.create_user("Testi", "Testi123")
        login = self.user_repo.login("Test1", "Testi321")
        self.assertEqual(login, False)

    def test_logout_works_correctly(self):
        self.user_repo.create_user("Testi", "Testi123")
        login = self.user_repo.login("Test1", "Testi123")
        self.user_repo.logout()
        user = self.user_repo.user
        self.assertEqual(user, None)
