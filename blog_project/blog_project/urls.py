from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
# from . import views
# from '/blog/views.py' import logout_view 
from blog.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Use blog app's URLs
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('ad/logout/', logout_view, name='logout'),
]