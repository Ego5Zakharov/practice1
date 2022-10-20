from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUser(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    add_fiedsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'fio',
                    'gender',
                    'birthday',
                    'groups',
                    'money'
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'fio',
                    'gender',
                    'birth_date',
                    'money'
                )
            }
        )
    )
