from django.db import models


class Gym(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)


class Workout(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    datetime = models.CharField(max_length=40)
    time = models.CharField(max_length=20)
    priceForWorkout = models.FloatField()
    gym = models.ForeignKey(Gym,
                            on_delete=models.CASCADE)  # 1 качалка может содержать в себе много различных тренировок

# КАЧАЛКА НИЧЕГО НЕ ДЕЛАЕТ!
# У КАЧАЛКИ ЕСТЬ ТОЛЬКО ИНДЕКС HTML

# Клиент может записываться на тренировки, КЛИЕНТ ЭТО ЮЗЕР(USER)
# модифицированный юзер

# тренировки - дефолт

# Администратор САМ СЛЕДИТ ЗА РАСПРЕДЕЛЕНИЕМ РОЛЕЙ МЕЖДУ ПЕРСОНАЛОМ
