# Generated by Django 5.0.6 on 2024-05-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='hours_played',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='star_rating',
            field=models.IntegerField(default=0),
        ),
    ]
