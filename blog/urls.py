from django.urls import path
from .views import blogs_list, blogs_detail, create_blog

urlpatterns = [
    path('', blogs_list, name="blogs_list"),
    path('detail/<int:pk>', blogs_detail, name='blog_detail'),
    path('create-blog', create_blog, name='create_blog_form')
]

