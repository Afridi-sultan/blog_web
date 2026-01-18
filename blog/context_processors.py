from blog.models import Category, Platform


def category_name(request):
    cate_name = Category.objects.all().order_by('-created_at')
    return dict(cate_name=cate_name)

def get_social_link(request):
    social_link = Platform.objects.all()
    return dict(social_link=social_link)