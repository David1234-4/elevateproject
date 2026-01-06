from django.urls import path
from . import views

urlpatterns = [
    path('',views.posts_list),
    path('courses/',views.courses),
    path('profiles/',views.profiles),
    path('downloads/',views.downloads),
]
