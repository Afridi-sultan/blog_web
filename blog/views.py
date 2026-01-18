from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from my_blog.forms import RegistrationForm
from .models import Blog, Category


def category_page(request,pk):
    cat_page = Blog.objects.filter(category=pk)
    cat_name = get_object_or_404(Category, pk=pk)
    context = {
        'cat_page': cat_page,
        'cat_name':cat_name
    }
    return render(request,'cat_page.html',context)

def slug_blog(request,slug):
    single_blog = Blog.objects.filter(slug=slug)
    context = {
        'single_blog':single_blog
    }
    return render(request,'slug_blog.html',context)

#search function
def search(request):
    input_form = request.GET.get('keyword')
    search_item = Blog.objects.filter(title__icontains=input_form)
    context = {
        'search_item': search_item
    }
    return render(request,'search.html',context)

#register user
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request,'register.html', context)

#login functionality
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard_url')
    form = AuthenticationForm()
    contex = {
        'form':form
    }
    return render(request,'login.html',contex)

#logout functionality
def logout(request):
    auth.logout(request)
    return redirect('home')
