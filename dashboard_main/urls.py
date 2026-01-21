from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard, name='dashboard_url'),
    #category urls
    path('category/',views.dashboard_category, name='dashboard_category'),
    path('blogs/',views.dashboard_blogs, name='dashboard_blogs'),
    path('add_category/',views.add_category, name='add_category'),
    path('delete_category/<int:pk>/',views.delete_category, name='delete_category'),
    path('category/<int:pk>/',views.edit_category,name='edit_category'),
    #blogs urls
    path('blogs/add_new_blog/',views.add_new_blog, name='add_new_blog'),
    path('blogs/edit_blog/<int:pk>/',views.edit_blog, name='edit_blog'),
    path('blogs/delete/<int:pk>/',views.delete_blog, name='delete_blog'),
]