from django.urls import path
from auth_app.views import *

from .views import register, user_login



urlpatterns = [
    path('register',register,name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
]