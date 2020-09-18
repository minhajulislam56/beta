# Generated by Django 3.1.1 on 2020-09-18 09:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_chatnew_messagenew'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatnew',
            name='user_list',
        ),
        migrations.AddField(
            model_name='chatnew',
            name='user_list',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
