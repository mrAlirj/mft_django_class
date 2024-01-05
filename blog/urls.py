from django.urls import path
from .views import blogs_list, blogs_detail

urlpatterns = [
    path('list', blogs_list, name="blogs_list"),
    path('detail/<int:pk>', blogs_detail, name='blog_detail')
]

