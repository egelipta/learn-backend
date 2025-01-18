from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)  # Primary key
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    full_name = fields.CharField(max_length=100, null=True)
    hashed_password = fields.CharField(max_length=100)
    
    class Meta:
        table = "users"

