from django.urls import path
from . import views

urlpatterns = [
    path("",views.indexpage),
    path("news",views.newspaper),
    path("sports",views.sportspage),
    path("politics",views.politics),
    path("national",views.nationalpage),
]
