from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="movie_index"),
    path("< movie_id >", views.detail, name="movie_detail")
]