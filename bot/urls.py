from django.urls import path
from bot.views import *
urlpatterns=[
    path('auth/createAccount',createAccount,name='createAccount'),
    path('auth/login',login,name='login'),
]