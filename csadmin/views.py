from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm, ProfileUpdateForm, UserUpdateForm, PostForm, CommentForm
from .models import Item, Profile, Post
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .middlewares import *

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('login')

    else:
        initial_data = {'username':'', 'email':'', 'password1':'', 'password2':'', 'first_name':'', 'last_name':''}
        form = UserForm(initial=initial_data)
    return render(request, 'register.html', {'form': form})
    
@guest    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'','password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def dashboard_view(request):
    post = Post.objects.all()
    form = CommentForm()
    return render(request, 'dashboard.html', {'post': post,'form':form})

@login_required
def profile_view(request, username):
    return render(request, 'profile.html', {'user': username})

@login_required
def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Do not save to the database yet
            post.user = request.user  # Set the user field
            post.save() 
            return redirect('dashboard')
    else:        
        form = PostForm()        
    return render(request, 'posts.html', {'form': form})

@login_required
def likes_view(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('dashboard')

@login_required
def comment_view(request,post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = Post.objects.get(id=post_id)
            comment.save()
            return redirect('dashboard')


@login_required
def delete_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('dashboard')

@login_required
def edit_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm(instance=post)
    return render(request, 'extras/editpost.html', {'form': form})



@login_required
def settings_view(request):
    video = Item.objects.all()
    return render(request, 'extras/settings.html', {'vid':video})


@login_required
def edit_profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=profile)
        u_form = UserUpdateForm(request.POST, instance=user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile', username=user.username)
    else:
        p_form = ProfileUpdateForm(instance=profile)
        u_form = UserUpdateForm(instance=user)
    return render(request, 'extras/editprofile.html', {'u_form': u_form,'p_form':p_form})

def logout_view(request):
    logout(request)
    return redirect('login')

