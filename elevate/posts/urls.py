from . import views
from django.urls import path
app_name = 'posts'

urlpatterns = [
    path('',views.posts_list,name='list'),
    path('<slug:slug>',views.post_page,name="page"),
    path('new-post/',view.post_new,name="new-post"),
]
