from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  
from django.shortcuts import redirect  # ✅
from django.contrib.auth.forms import UserCreationForm

from django.core.paginator import Paginator
from .models import BlogPost
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import BlogPost
from django.views.decorators.csrf import csrf_exempt
def blog_list(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(blog_posts, 10)  # Show 10 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})

def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog_post': blog_post})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # Set the author to the logged-in user
            blog_post.save()
            return redirect('blog_list')  # Redirect to the blog list page after saving
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def edit_blog(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        pass# Handle form submission for editing the blog post
    else:
        # Render form pre-filled with blog post data for editing
        return render(request, 'blog/edit_blog.html', {'blog_post': blog_post})

@login_required
def delete_blog(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    # Handle delete logic and redirect to blog list
@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signing up
            return redirect('blog_list')  # Redirect to blog list
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
@csrf_exempt
def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to home or another page
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})
def home(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')[:10]  # Get the 10 most recent blog posts
    
    context = {
        'blog_posts': blog_posts,
    }
    
    return render(request, 'home.html', context)
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
@csrf_exempt
def login_view(request):
    return render(request, 'registration/login.html')

@login_required
def logout_view(request):
    # logout(request)
    if request.method == "POST" or request.method == "GET":  # Allow both methods
        logout(request)
        blog_posts = BlogPost.objects.order_by('-created_at')[:10] 
        #blogs = Blog.objects.order_by('-created_at')[:10]  # Get the 10 most recent blogs
        return render(request, 'home.html', {'blog_posts': blog_posts})
        # return redirect('home')
    # return redirect('home')
def user_logout(request):
    logout(request)
    return redirect('home')