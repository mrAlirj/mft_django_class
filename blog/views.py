from django.shortcuts import render, redirect

from accounts.models import User
from .models import Blog


def blogs_list(request):
    blogs = Blog.objects.all().order_by('-create_date')
    return render(request, 'blog/blogs_list.html', context={"blogs": blogs})


def blogs_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/blog_detail.html', context={"blog": blog})


def create_blog(request):
    if request.method == 'GET':
        users = User.objects.all()
        context = {'users': users}
        return render(request, 'blog/create_blog.html',  context=context)
    else:
        title = request.POST.get('title')
        matne_khabar = request.POST.get('body')
        nevisande = request.POST.get('author')
        Blog.objects.create(title=title, body=matne_khabar, author_id=nevisande)
        return redirect("blogs_list")
