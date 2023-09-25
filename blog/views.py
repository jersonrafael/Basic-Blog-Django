from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,authenticate

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Post
from .forms import CreatePost

from django.utils import timezone


# Create your views here.
def home(request):
    user = User
    post = Post.objects.all()
    creator = User.objects.all().values()
    template = get_template('home.html')
    context = {
        "post":post,
        "userCreator":creator,
        "user": request.user,
    }
    return HttpResponse(template.render(context,request))


@login_required
def createPost(request):
    if request.method == "POST":
        postName = request.POST.get('postName')
        postDescript = request.POST.get('postDescript')
        postCreator = request.user
        date = timezone.now()
        Post.objects.create(
            postName=postName,
            postDescript=postDescript,
            postCreator = postCreator,
            dateCreate = date
        )
        return redirect('home')
    form = CreatePost
    template = get_template('createPost.html')
    context = {
        "form":form
    }
    return HttpResponse(template.render(context,request))

def post(request,pk):
    template = get_template('post.html')
    post = Post.objects.filter(id=pk)
    context = {
        "post":post
    }
    return HttpResponse(template.render(context,request))

@login_required
def deletepost(request,pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    if post:
        post.delete()
        # return redirect(f'profile/{id}')
        return redirect(f'/profile/{user.id}')
    else:
        return HttpResponse(f'Post {pk} Not Found')


def login_view(request):
    if request.method == 'POST':
        template = get_template('login.html')
        user = authenticate(request,username=request.POST['username'],password=request.POST['password']) 
        if user is None:
            context ={
                "form":AuthenticationForm,
                "error":"The username or the password are wrong"
            }
            return HttpResponse(template.render(context,request))
        else:
            login(request,user)
            return redirect('home')
        
    template = get_template('login.html')
    context = {
        "form":AuthenticationForm
    }
    return HttpResponse(template.render(context,request))

@login_required
def logOut_view(request):
    logout(request)
    return redirect('home')

def create_account(request):
    form = UserCreationForm
    template = get_template('register.html')
    context = {
        "form":UserCreationForm
    }
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                context = {'form':UserCreationForm,'error':'Username already taken. Choose new username.'}
                return HttpResponse(template.render(context,request))
        else:
            context = {'form':UserCreationForm, 'error':'Passwords do not match'}
            return HttpResponse(template.render(context,request))
    else:
        return HttpResponse(template.render(context,request))
    
@login_required
def profile(request,pk):
    template = get_template('myprofile.html')
    find = User.objects.filter(id=pk)
    post = Post.objects.filter(postCreator=pk)
    context = {
        "user":request.user,
        "post":post
    }
    return HttpResponse(template.render(context,request))