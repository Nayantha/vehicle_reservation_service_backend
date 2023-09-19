from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password_hash = fields.CharField(256)

    @classmethod
    async def get_user(cls, username):
        """
        Get user fom username.
        :param username: Username of the user        :return:
        """
        return cls.get(username=username)
