from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'accounts'
urlpatterns = [
    path('index/', views.HomeView.as_view(template_name='accounts/home.html'), name='home'),
    path('login',views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register')
]
