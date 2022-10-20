from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )
    fio = models.CharField('ФИО', max_length=255, default='')
    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateTimeField('Дата рождения', default='2004-05-26')
    money = models.FloatField(default='0')