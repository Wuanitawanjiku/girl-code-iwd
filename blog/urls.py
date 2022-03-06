from django.urls import path
from .views import blog_home,write_blog
urlpatterns =[
    path('home/',blog_home, name='blog_home'),
    path('upload-blog/',write_blog, name='upload-blog'),
]