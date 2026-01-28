from django.urls import path
from . import views

urlpatterns = [
    path('', views.download_list, name='download_list'),
    path('watch/<int:file_id>/', views.stream_video, name='stream_video'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]
