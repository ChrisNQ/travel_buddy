from __future__ import unicode_literals
from ..loginreg.models import User
from django.db import models

class Travel(models.Model):
    name = models.CharField(max_length = 50)
    destination = models.TextField(max_length = 50)
    description = models.TextField(max_length = 100)
    start_date = models.TextField(max_length = 50)
    end_date = models.TextField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    users = models.ManyToManyField(User)

class TravelUser(models.Model):
    user = models.ForeignKey('loginreg.user', default = None)
    travels = models.ForeignKey('travels.travel', default = None)
