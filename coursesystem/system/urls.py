# accounts/urls.py

from django.urls import path
from .views import home, signup, login_view

urlpatterns = [
    path('', home, name='home'),  # Set home page as the default path
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
]
