# accounts/urls.py

from django.urls import path
from .views import home, logout_view, signup, login_view

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
      path('logout/', logout_view, name='logout'),
]
