from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),  # index view at /
    # likepost view at /likepost
    path('likepost/', views.likePost, name='likepost'),
]
