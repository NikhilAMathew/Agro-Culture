# Generated by Django 4.0.2 on 2022-04-07 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labappointment',
            name='lab',
        ),
    ]
