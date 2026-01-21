from django import forms
from blog.models import Category, Blog, Platform, About

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

#Blog form class
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','featured_image','short_description','blog_body','status','is_featured',)

#Platforms links
class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = '__all__'
#About
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'