# Generated by Django 3.2.13 on 2022-11-17 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=50)),
                ('character_MBTI_type', models.CharField(max_length=4)),
                ('original_movie_title', models.TextField()),
                ('movie_title', models.TextField()),
                ('character_img_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MBTI_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=4)),
                ('description', models.TextField()),
                ('bad_match', models.ManyToManyField(related_name='_mbti_compabilities_mbti_type_bad_match_+', to='mbti_compabilities.MBTI_Type')),
                ('good_matching', models.ManyToManyField(related_name='good_matched', to='mbti_compabilities.MBTI_Type')),
            ],
        ),
    ]
