from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Category, Blog

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