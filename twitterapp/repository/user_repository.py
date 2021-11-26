
from typing import Type
from twitterapp.models import User


class userRepository():

    def __init__(self,User: Type[User]):
        self.user = User

    def findall_users(self)-> User:
        return self.user.filter(state=True).values()

    def findbyid_users(self,id: int)-> User:
        users = self.user.objects.filter(id=id)
        return users


    def create_user(self, **users) -> User:
        try:
            user =self.user()
            user.name = users.get('name')
            user.telefone = users.get('telefone')
            user.email = users.get('email')
            user.password = users.get('password')
            result_user = user.save()
            return  result_user
        except Exception as e:
            raise e

    def delete_user(self, id)-> User:
        return self.user.objects.filter(id=id).update(state=False)