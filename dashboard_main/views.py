from timeit import reindent

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Category, Blog, Platform, About
from dashboard_main.forms import CategoryForm, BlogForm, PlatformForm, AboutForm, AddUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
@login_required(login_url='login_page')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    platform_count = Platform.objects.all().count()
    context = {
        'category_count':category_count,
        'blog_count':blog_count,
        'platform_count':platform_count
    }
    return render(request,'dashboard/dashboard.html',context)

#user dashboard category
def dashboard_category(request):
    return render(request,'dashboard/category.html')
@login_required(login_url='login_page')
#user dashboard blogs
def dashboard_blogs(request):
    all_blogs = Blog.objects.all().order_by('-created_at')
    context = {
        'all_blogs':all_blogs
    }
    return render(request,'dashboard/blogs.html',context)

#add category in dashboard
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_category')
    else:
        form = CategoryForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_category.html',context)

#delete the category from the dashboard
def delete_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('dashboard_category')

#Edit category from dashboard
def edit_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard_category')
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category
    }
    return render(request, 'dashboard/edit_category.html',context)

#Add new blog from dashboard
def add_new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            temporary_save = form.save(commit=False)
            temporary_save.author = request.user
            temporary_save.save()
            title = form.cleaned_data['title']
            temporary_save.slug = slugify(title)+ '-'+str(temporary_save.id)
            temporary_save.save()
            return redirect('dashboard_blogs')
    form = BlogForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_blog.html',context)
#Edit blog functionality
def edit_blog(request,pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            temporary_save = form.save(commit=False)
            title = form.cleaned_data['title']
            temporary_save.slug = slugify(title)+'-'+str(temporary_save.id)
            temporary_save.save()
            return redirect('dashboard_blogs')
    form = BlogForm(instance=blog)
    context = {
        'form':form,
        'blog':blog,
    }
    return render(request,'dashboard/edit_blog.html',context)
#Delete blog functionality
def delete_blog(request,pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('dashboard_blogs')

#add platform links
def platform(request):

    return render(request,'dashboard/platform.html')

#Edit platform
def edit_platform(request,pk):
    all_platform = get_object_or_404(Platform, pk=pk)
    if request.method == 'POST':
        form = PlatformForm(request.POST, instance=all_platform)
        if form.is_valid():
            form.save()
            return redirect('platform')
    form = PlatformForm(instance=all_platform)
    context = {
        'form':form,
        'all_platform':all_platform,
    }
    return render(request,'dashboard/edit_platform.html', context)

#Add platform
def add_platform(request):
    if request.method == 'POST':
        form = PlatformForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('platform')
    form = PlatformForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_platform.html',context)

#delete platform
def delete_platform(request,pk):
    all_platform = get_object_or_404(Platform, pk=pk)
    all_platform.delete()
    return redirect('platform')

#about dynamic =======================================
#add about
def about(request):
    all_about = About.objects.all()
    count_about = About.objects.all().count()
    context = {
        'about_details':all_about,
        'count_about':count_about,
    }
    return render(request,'dashboard/about.html',context)

#Edit about
def edit_about(request,pk):
    all_about = get_object_or_404(About, pk=pk)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=all_about)
        if form.is_valid():
            form.save()
            return redirect('about')
    form = AboutForm(instance=all_about)
    context = {
        'form':form,
        'all_about':all_about,
    }
    return render(request,'dashboard/edit_about.html', context)

#Add about
def add_about(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('about')
    form = AboutForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_about.html',context)

#delete about
def delete_about(request,pk):
    all_about = get_object_or_404(About, pk=pk)
    all_about.delete()
    return redirect('about')

#fetch users ==================================
def users(request):
    all_user = User.objects.all()
    context = {
        'all_user':all_user,
    }
    return render(request,'dashboard/users.html',context)

#add new user
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')

    form = AddUserForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_user.html',context)

#edit user
def edit_user(request,pk):
    main_user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = AddUserForm(request.POST, instance=main_user)
        if form.is_valid():
            form.save()
            return redirect('users')

    form = AddUserForm(instance=main_user)
    context = {
        'form':form,
        'main_user':main_user,
    }

    return render(request,'dashboard/edit_user.html',context)