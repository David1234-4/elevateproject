from . import views
from django.urls import path
app_name = 'users'

urlpatterns = [
    path('register/',views.register_users,name='register'),
    path('login/',views.login_users,name='login'),
    path('logout/',views.login_users,name='logout'),
]
