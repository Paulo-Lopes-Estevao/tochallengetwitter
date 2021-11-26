import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
import django

django.setup()
from django.core.management import call_command
import unittest

from twitterapp.usecase.interactor.user_interactor import userInteractor
from twitterapp.repository.user_repository import userRepository


class UserRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        self.user_interactor = userInteractor(userRepository=userRepository)

    def test_create_user(self):
        data_user = {"name": 'John', 'telefone': '923453925', 'email': "pl@gmail.com", 'password': '1234'}
        user = self.user_interactor.addUsers(**data_user)
        self.assertEqual(user.get('email'), data_user.get('email'), "usuario cadastrado")

    def test_get_all_users(self):
        users =self.user_interactor.getUsers()
        self.assertGreaterEqual(len(users),1)

    def test_delete_user(self):
        users = self.user_interactor.deletebyidUsers("ef5da2dc-3b46-4d30-92f2-154f6f75f1ad")
        self.assertTrue(users)

if __name__ == '__main__':
    unittest.main()
