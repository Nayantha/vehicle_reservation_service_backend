from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    email = fields.CharField(50, unique=True)
    contact_number = fields.CharField(10, unique=True)
    password_hash = fields.CharField(256)

    @classmethod
    async def get_user(cls, username):
        """
        Get user fom username.
        :param username: Username of the user        :return:
        """
        return cls.get(username=username)

    def verify_password(self, password: str):
        return self.password_hash == password
