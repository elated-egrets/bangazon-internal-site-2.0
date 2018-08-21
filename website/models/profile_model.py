from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    '''Model for viewing the profile of logged in User

    Arguments:
        models {[user]} -- one to one relationship to profile to access the key
                address -- character field to gather address info
                phone --- integar field for phone number
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    phone = models.IntegerField()
