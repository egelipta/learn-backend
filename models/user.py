from tortoise import fields
from tortoise.models import Model
from datetime import datetime

class TimestampMixin(Model):
    create_time = fields.DatetimeField(default=datetime.now)
    update_time = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True

class User(TimestampMixin):
    id = fields.IntField(pk=True) 
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    full_name = fields.CharField(max_length=100, null=True)
    password = fields.CharField(max_length=100)

    class Meta:
        table = "users"
