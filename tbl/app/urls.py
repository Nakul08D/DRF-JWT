from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name= 'home'),
    path('signup/',CustomUserCreateView.as_view(), name= 'signup'),
    path('login/',CustomLoginView.as_view(), name= 'login')
]
