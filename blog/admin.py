from django.contrib import admin
from .models import Category,Blog,About, Platform,BlogComment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','category','author','status','is_featured')
    search_fields = ('id','title','category__category_name')

# disabled add button if more than 0
class AboutSetting(admin.ModelAdmin):
    def has_add_permission(self, request):
        about = About.objects.all().count()
        if about == 0:
            return True
        return False

admin.site.register(Category)
admin.site.register(Platform)
admin.site.register(About,AboutSetting)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
