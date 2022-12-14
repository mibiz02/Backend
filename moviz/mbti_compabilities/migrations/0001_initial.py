# Generated by Django 3.2.13 on 2022-11-22 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_tmdb_id', models.IntegerField()),
                ('character_name', models.CharField(max_length=50)),
                ('character_MBTI_type', models.CharField(max_length=4)),
                ('movie_title', models.TextField()),
                ('character_img_path', models.TextField()),
                ('movie_img_path', models.TextField()),
                ('movie_backdrop_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MBTI_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=4)),
                ('description', models.TextField()),
                ('bad_matching', models.ManyToManyField(related_name='bad_matched', to='mbti_compabilities.MBTI_Type')),
                ('good_matching', models.ManyToManyField(related_name='good_matched', to='mbti_compabilities.MBTI_Type')),
            ],
        ),
        migrations.CreateModel(
            name='MBTI_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mbti_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbti_compabilities.mbti_type')),
            ],
        ),
    ]
