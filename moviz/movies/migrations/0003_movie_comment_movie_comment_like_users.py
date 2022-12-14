# Generated by Django 3.2.13 on 2022-11-22 13:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_movie_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_comment',
            name='movie_comment_like_users',
            field=models.ManyToManyField(related_name='like_movie_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
