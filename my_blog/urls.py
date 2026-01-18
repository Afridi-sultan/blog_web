from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('category/',include('blog.urls')),
    path('<slug:slug>/', include('blog.urls')),
    path('dashboard/', include('dashboard_main.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

