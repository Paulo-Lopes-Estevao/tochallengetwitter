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


if __name__ == '__main__':
    unittest.main()
