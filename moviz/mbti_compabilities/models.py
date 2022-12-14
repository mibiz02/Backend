from django.db import models
from django.conf import settings

# Create your models here.
class MBTI_Type(models.Model):
    letter = models.CharField(max_length=4)
    description = models.TextField()
    good_matching = models.ManyToManyField('self', symmetrical=False, related_name='good_matched')
    bad_matching = models.ManyToManyField('self', symmetrical=False, related_name='bad_matched')
    def __str__(self):
        return self.id


class MBTI_Comment(models.Model):
    content = models.TextField()
    mbti_type = models.ForeignKey(MBTI_Type, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_mbti_comments")
    
    def __str__(self):
        return self.content


class Character(models.Model):
    movie_tmdb_id = models.IntegerField()
    character_name = models.CharField(max_length=50)
    character_MBTI_type = models.CharField(max_length=4)
    movie_title = models.TextField()
    character_img_path = models.TextField()
    movie_img_path = models.TextField()
    movie_backdrop_path = models.TextField()
    
    def __str__(self):
        return self.character_name