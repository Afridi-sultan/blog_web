from django.shortcuts import render
from blog.models import Blog, About, Platform


def home(request):
    #managed categories name by context_processors.py
    # categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True).order_by('-created_at')
    not_featured = Blog.objects.filter(is_featured=False, status=0)
    #fetch about
    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        # 'categories':categories,
        'featured_post':featured_post,
        'not_featured':not_featured,
        'about':about,

    }
    return render(request,'home-blogs.html',context)

