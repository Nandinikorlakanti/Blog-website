"""from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

from .views import user_logout
from blog import views
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/create/', views.create_blog, name='create_blog'),
    path('blog/<int:pk>/edit/', views.edit_blog, name='edit_blog'),
    path('blog/<int:pk>/delete/', views.delete_blog, name='delete_blog'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),  # ✅ Add this line
    path('', views.home, name='home'),
    
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
   """
    
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.home, name='home'),  # Home page should be first
    path('blog/', views.blog_list, name='blog_list'),  # Correct blog list URL
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/create/', views.create_blog, name='create_blog'),
    path('blog/<int:pk>/edit/', views.edit_blog, name='edit_blog'),
    path('blog/<int:pk>/delete/', views.delete_blog, name='delete_blog'),
    path('create/', views.create_blog, name='create_blog'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('blogs/', views.blog_list, name='blog_list'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])