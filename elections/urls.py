
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('vote/', views.vote, name='vote'),
]