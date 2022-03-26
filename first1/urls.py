from django.urls import path
from . import views


urlpatterns = [
    path('', views.azzani, name='azzani-blog'),
    path ('janeen/', views.janeen, name='janeen-blog'),
]
