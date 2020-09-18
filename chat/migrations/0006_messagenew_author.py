# Generated by Django 3.1.1 on 2020-09-18 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_auto_20200918_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagenew',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
