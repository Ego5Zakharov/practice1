import users
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, LoginView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class AuthenticationForm(LoginView):
    template_name = 'login.html'

def post(self, request, *args, **kwargs):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()

        for form_ug in form.cleaned_data['groups']:
            user_group = Group.objects.get(name=form_ug.name)
            user.groups.add(user_group)
        return redirect('login')
    else:
        return render(request, self.template_name, {'form': form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/users/login')


