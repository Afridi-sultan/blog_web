from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard, name='dashboard_url'),
    path('category/',views.dashboard_category, name='dashboard_category'),
    path('blogs/',views.dashboard_blogs, name='dashboard_blogs')
]