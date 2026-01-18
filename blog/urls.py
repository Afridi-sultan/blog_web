from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/',views.category_page, name='category_page'),
    path('single-blog/',views.slug_blog, name='slug_blog'),
    path('blog/search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/',views.login, name='login_page'),
    path('logout/',views.logout, name='logout')

]