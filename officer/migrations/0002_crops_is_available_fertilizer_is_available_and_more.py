# Generated by Django 4.0.2 on 2022-04-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crops',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fertilizer',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='irrigation',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pesticide',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]