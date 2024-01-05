from django.shortcuts import render
from .models import Blog


def blogs_list(request):
    blogs = Blog.objects.all().order_by('-create_date')
    return render(request, 'blogs_list.html', context={"blogs": blogs})


def blogs_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog_detail.html', context={"blog": blog})
