# Generated by Django 4.1.6 on 2023-02-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_clubs_sports_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(default='', max_length=50)),
                ('sun', models.TextField(default='')),
                ('mon', models.TextField(default='')),
                ('tue', models.TextField(default='')),
                ('wed', models.TextField(default='')),
                ('thu', models.TextField(default='')),
                ('fri', models.TextField(default='')),
                ('sat', models.TextField(default='')),
            ],
        ),
    ]
