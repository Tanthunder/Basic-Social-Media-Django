from django.shortcuts import render , redirect
from.forms import LoginForm , UserRegistrationForm
from django.contrib.auth import authenticate , login ,decorators
from django.http import HttpResponse
from django.contrib.auth.models import User
from . models import Profile
from .forms import ProfileEditForm, UserEditForm
from posts.models import Post

# Create your views here.

def user_login(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponse("authenticated and logged in")
            else:
                return HttpResponse("Check credentials")

    form = LoginForm()

    return render (request, 'users/login.html', {'form':form})


@decorators.login_required
def index(request):
    current_user = request.user
    posts = Post.objects.filter(user = current_user)
    profile = Profile.objects.filter(user=current_user).first()
    return render (request, 'users/index.html',{'posts':posts,'profile':profile})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            
            first_name = form.cleaned_data['first_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            #user= form.save(commit = false) can also work
            user = User(username=username,first_name = first_name )
            user.set_password(password)
            user.save()
            Profile.objects.create(user = user)
            return redirect('login')
    form = UserRegistrationForm()
    return render (request, 'users/register.html', {'form' : form})

@decorators.login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data = request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data = request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    return render (request, 'users/edit.html',{'user_form':user_form,'profile_form':profile_form})
    



