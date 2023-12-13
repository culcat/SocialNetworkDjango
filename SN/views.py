from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import Post


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'SN/login.html', {'form': form})
def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Use password1 for the password field
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'SN/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
def post_view(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        if post_id:
            post= get_object_or_404(Post, pk=post_id)
            user = request.user
            if user in post.likes.all():
                post.likes.remove(user)
            else:
                post.likes.add(user)
    return render(request,'SN/index.html', {'posts': posts})