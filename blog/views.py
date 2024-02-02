from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import User
from .models import Blog
from .forms import BlogForm

# @login_required
# def blogs_list(request):
#     blogs = Blog.objects.all().order_by('-create_date')
#     return render(request, 'blog/blogs_list.html', context={"blogs": blogs})



# def blogs_list(request):
#     blogs = Blog.objects.all().order_by('-create_date')
#     if request.user.is_authenticated:
#         return render(request, 'blog/blogs_list.html', context={"blogs": blogs})
#     return render(request, 'blog/blogs_list.html')

class BlogsList(LoginRequiredMixin, ListView):
    queryset = Blog.objects.filter(is_publish=True).order_by('-create_date')
    template_name = 'blog/blogs_list.html'
    context_object_name = 'blogs'


# def blogs_detail(request, pk):
#     blog = Blog.objects.get(pk=pk)
#     return render(request, 'blog/blog_detail.html', context={"blog": blog})

class BlogsDetail(DetailView):
    queryset = Blog.objects.all()
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'


def create_blog(request):
    blog_form = BlogForm()
    if request.method == 'GET':
        users = User.objects.all()
        context = {'form': blog_form, 'users': users}
        return render(request, 'blog/create_blog.html', context=context)
    else:
        title = request.POST.get('title')
        matne_khabar = request.POST.get('body')
        nevisande = request.POST.get('author')
        Blog.objects.create(title=title, body=matne_khabar, author_id=nevisande)
        return redirect("blogs_list")
