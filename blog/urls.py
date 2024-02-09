from django.urls import path
from .views import BlogsList, blogs_detail, create_blog, author_blogs

urlpatterns = [
    path('', BlogsList.as_view(), name="blogs_list"),
    path('detail/<int:pk>', blogs_detail, name='blog_detail'),
    path('create-blog', create_blog, name='create_blog_form'),
    path('author-blogs', author_blogs, name='author_blogs'),
]

