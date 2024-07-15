# Generated by Django 5.0.6 on 2024-07-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_hours_played_comment_star_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='hours_played',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='star_rating',
        ),
        migrations.AddField(
            model_name='comment',
            name='starRating',
            field=models.IntegerField(default=0, help_text='Rate this comment from 1 to 5.'),
        ),
    ]