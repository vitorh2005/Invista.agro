from django.urls import path

from . import views

urlpatterns = [
path('', views.index, name="index"),
path('sobre/', view.sobre, name='sobre'),
]