from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from accounts.models import User
from .models import Blog, Comment
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

class BlogsList(ListView):
    queryset = Blog.objects.filter(is_publish=True).order_by('-create_date')
    template_name = 'blog/blogs_list.html'
    context_object_name = 'blogs'



@login_required
def author_blogs(request):
    user = request.user
    if user.is_writer:
        user_blogs = user.blogs.all()
        context = {
            'author_blogs': user_blogs
        }
        return render(request, 'blog/author_blogs.html', context=context)
    return HttpResponse("شما به این صفحه دسترسی ندارید.")


@login_required
def blogs_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    blogs_commnets = blog.comments.filter(reply__isnull=True)
    commnet_replies = Comment.objects.filter(blog=blog, reply__isnull=False)
    return render(request, 'blog/blog_detail.html', context={
        "blog": blog, 
        'comments': blogs_commnets,
        'replies': commnet_replies
        })

# class BlogsDetail(LoginRequiredMixin, DetailView):
#     queryset = Blog.objects.all()
#     template_name = 'blog/blog_detail.html'
#     context_object_name = 'blog'


@login_required
def create_blog(request):
    blog_form = BlogForm()
    if request.method == 'GET':
        users = User.objects.filter(is_writer=True)
        context = {'form': blog_form, 'users': users}
        return render(request, 'blog/create_blog.html', context=context)
    else:
        title = request.POST.get('title')
        matne_khabar = request.POST.get('body')
        nevisande = request.POST.get('author')
        Blog.objects.create(title=title, body=matne_khabar, author_id=nevisande)
        return redirect("blogs_list")
