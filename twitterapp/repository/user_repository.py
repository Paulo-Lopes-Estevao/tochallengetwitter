
from typing import Type
from twitterapp.models import User


class userRepository():

    def __init__(self,User: Type[User]):
        self.user = User()

    def findall_users(self) -> User:
        return self.user

    def findbyid_users(self,id: int)-> User:
        users = self.user.objects.filter(id=id)
        return users


    def create_user(self, **users) -> User:
        try:
            self.user.name = users.get('name')
            self.user.telefone = users.get('telefone')
            self.user.email = users.get('email')
            self.user.password = users.get('password')
            user = self.user.save()
            return  user
        except Exception as e:
            raise e

    def delete_user(self, id)-> User:
        return self.user.objects.filter(id=id).update(state=False)