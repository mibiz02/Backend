from django.urls import path
from .  import views

app_name='movies'
urlpatterns = [
    path('list/', views.movie_lst),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_detail)
]
