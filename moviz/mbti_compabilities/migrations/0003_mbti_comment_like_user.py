# Generated by Django 3.2.13 on 2022-11-22 15:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mbti_compabilities', '0002_mbti_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbti_comment',
            name='like_user',
            field=models.ManyToManyField(related_name='like_mbti_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
