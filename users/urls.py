from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('logout/', log_out, name='logout'),
    path('login/', login_view, name='login'),
]