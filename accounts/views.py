from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        print(request.POST)
        print(form.cleaned_data)
        # print(form.is_valid())
        # print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("blogs_list")
        
        return render(request, "accounts/register_user.html", {"form": form})
    else:
        form = RegisterForm()

    return render(request, "accounts/register_user.html", {"form": form})



def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        print(form.cleaned_data)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('blogs_list')
            return redirect("registration")
        
        # form is not valid or user is not authenticated
        return render(request,'registration/login.html',{'form': form})
