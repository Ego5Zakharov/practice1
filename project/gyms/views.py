import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from gyms.models import Gym

from gyms.models import Workout


def index(request):
    workouts = Workout.objects.all()
    return render(request, "index.html", {"workouts": workouts})


# добавление данных из бд
@login_required
def create(request):

    createGym()

    # если запрос POST, сохраняем данные
    if request.method == "POST":
        workout = Workout()
        workout.name = request.POST.get("name")
        workout.description = request.POST.get("description")
        workout.datetime = request.POST.get("datetime")
        workout.time = request.POST.get("time")
        workout.priceForWorkout = request.POST.get("priceForWorkout")

        workout.gym_id = request.POST.get("gym")
        workout.save()
        return HttpResponseRedirect("")
    # передаем данные в шаблон
    gyms = Gym.objects.all()
    return render(request, "create.html", {"gyms": gyms})

@login_required
# изменение данных в бд
def edit(request, id):
    try:
        workout = Workout.objects.get(id=id)

        if request.method == "POST":
            workout.name = request.POST.get("name")
            workout.description = request.POST.get("description")
            workout.datetime = request.POST.get("datetime")
            workout.time = request.POST.get("time")
            workout.priceForWorkout = request.POST.get("priceForWorkout")

            workout.gym_id = request.POST.get("gym")
            workout.save()
            return HttpResponseRedirect("/")
        else:
            gyms = Gym.objects.all()
            return render(request, "edit.html", {"workout": workout, "gyms": gyms})
    except Workout.DoesNotExist:
        return HttpResponseNotFound("<h2>Workout not found</h2>")

@login_required
# удаление данных из бд
def delete(request, id):
    try:
        workout = Workout.objects.get(id=id)
        workout.delete()
        return HttpResponseRedirect("/")
    except Workout.DoesNotExist:
        return HttpResponseNotFound("<h2>Workout not found</h2>")

def createGym():
    if Gym.objects.all().count() == 0:
        Gym.objects.create(name="ArnoldClassic1", address="Сыгынак 47/1")
        Gym.objects.create(name="ArnoldClassic2", address="Сыгынак 47/2")
        Gym.objects.create(name="ArnoldClassic3", address="Сыгынак 47/3")
