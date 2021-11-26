
from typing import Type
from twitterapp.models import User


class userRepository():

    def __init__(self,User: Type[User]):
        self.user = User

    def findall_users(self):
        return self.user

    def findbyid_users(self,id: int):
        users = self.user.objects.filter(id=id)
        return users


    def create_user(self, **users):
        self.user.name = users.get('name')
        self.user.telefone = users.get('telefone')
        return self.user.save()

    def delete_user(self, id):
        self.user.objects.filter(id=id).update(state=False)