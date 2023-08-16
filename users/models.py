from django.db import models

from django.contrib.auth.models import AbstractUser

class UsersModel(AbstractUser):
    pass



class ApiUserModel(models.Model):
    telegram_id = models.CharField(max_length=150)
    lang = models.CharField(max_length=2, default='uz')


    def __str__(self):
        return self.telegram_id
    

