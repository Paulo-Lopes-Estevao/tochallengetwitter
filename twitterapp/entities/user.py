from twitterapp.models import User as userModel


class User:

    def __init__(self):
        self.user_model = userModel()

    def addUsers(self, **user):
        try:
            return self.passwordEncrypt(**user)
        except Exception as e:
            raise e

    def passwordEncrypt(self, **user):
        self.user_model.set_password(user.get('password'))
        user['password'] = self.user_model.password
        return self.validate(**user)

    def validate(self, **user):
        print(user)
        for k in user.values():
            if k in "":
                return "Not Valid"
        return user
