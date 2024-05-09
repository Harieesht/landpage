from django.urls import path
from .views import UserCreate,get_csrf_token

urlpatterns=[
    path('create',UserCreate,name='Usercreation'),
    path('get_csrf_token',get_csrf_token,name='get_csrf_token'),
]