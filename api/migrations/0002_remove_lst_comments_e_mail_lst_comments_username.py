# Generated by Django 4.1.6 on 2023-02-17 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lst_comments',
            name='e_mail',
        ),
        migrations.AddField(
            model_name='lst_comments',
            name='username',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='lst_cmnt_username', to=settings.AUTH_USER_MODEL),
        ),
    ]
