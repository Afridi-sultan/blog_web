from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Category, Blog
from dashboard_main.forms import CategoryForm
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