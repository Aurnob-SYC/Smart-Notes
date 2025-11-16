from django.urls import path
from . import views

urlpatterns = [
    path('', views.feature_notes, name='notes'),
    path('create_notes/', views.create_notes, name='create_notes'),
    path('my_notes/', views.my_notes, name='my_notes'),
]
