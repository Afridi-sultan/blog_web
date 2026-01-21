from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Category, Blog
from dashboard_main.forms import CategoryForm, BlogForm
from django.template.defaultfilters import slugify

@login_required(login_url='login_page')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context = {
        'category_count':category_count,
        'blog_count':blog_count
    }
    return render(request,'dashboard/dashboard.html',context)

#user dashboard category
def dashboard_category(request):
    return render(request,'dashboard/category.html')

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