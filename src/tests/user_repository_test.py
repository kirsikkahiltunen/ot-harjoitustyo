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

    def test_login_works_correctly(self):
        self.user_repo.create_user("Testi", "Testi123")
        login = self.user_repo.login("Testi", "Testi123")
        self.assertEqual(login, True)
