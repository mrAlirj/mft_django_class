from django.urls import path
from .views import BlogsList, BlogsDetail, create_blog

urlpatterns = [
    path('', BlogsList.as_view(), name="blogs_list"),
    path('detail/<int:pk>', BlogsDetail.as_view(), name='blog_detail'),
    path('create-blog', create_blog, name='create_blog_form')
]

