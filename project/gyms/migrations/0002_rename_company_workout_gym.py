# Generated by Django 4.1.2 on 2022-10-17 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='company',
            new_name='Gym',
        ),
    ]
