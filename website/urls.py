from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('contact/', views.contact_page, name='contact'),
    path('about/', views.about_page, name='about'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('dashboard/', views.dashboard_page, name='dashboard'),
    path('dashboard/notes/', views.feature_notes, name='notes'),
]