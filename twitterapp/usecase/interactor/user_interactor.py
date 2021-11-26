from typing import Type
from twitterapp.entities.user import User
from twitterapp.models import User as userModel
from twitterapp.repository.user_repository import userRepository

class userInteractor:

    def __init__(self, userRepository: Type[userRepository]):
        self.user_repository = userRepository(User=userModel)

    def getUsers(self)-> userModel:
        return self.user_repository.findall_users()

    def getByIdUsers(self, id: int):
        return self.user_repository.findbyid_users(id)

    def addUsers(self, **user) -> userModel:
        users = User().addUsers(**user)
        self.user_repository.create_user(**users)
        return users

    def deletebyidUsers(self, id) -> userModel:
        return self.user_repository.delete_user(id)