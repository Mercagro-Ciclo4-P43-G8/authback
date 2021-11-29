from django.db import models
from .user import User

class Account(models.Model):
    id              = models.AutoField(primary_key=True)
    user            = models.ForeignKey(User, related_name="account", on_delete=models.CASCADE)
    balance          = models.IntegerField(default=0)
    last_date_change = models.DateTimeField()
    is_activate      = models.BooleanField(default=True)