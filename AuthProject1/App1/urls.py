from django.urls import path
from .views import loginView, registerView, logoutView, home, result

urlpatterns = [
    path('login/', loginView, name = 'login'),
    path('register/', registerView, name = 'register'),
    path('logout/', logoutView, name='logout'),
    path('home/', home, name='home'),
    path('result/', result, name='result'),

]