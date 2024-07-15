from functools import cache
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.db.models import Q
from django.contrib.auth import login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from auth_app.models import  PostModel, comments
from .form import CommentForm, PostModelForm, TagForm

def register_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data ={'username':'','password1':'','password2':''}
        form=UserCreationForm(initial=initial_data)
    return render(request,'auth/register.html',{'form':form})
    
    
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data ={'username':'','password':''}
        form=AuthenticationForm(initial=initial_data)
    return render(request,'auth/login.html',{'form':form})

def logout_view(request):
   logout(request)
   return redirect('login')

def dashboard_view(request):
    searching = request.GET.get('search', '')
    posts = PostModel.objects.filter(Q(title__icontains=searching))
    return render(request, 'dashboard.html', {'posts': posts})



@login_required(login_url='login')
def create_blog(request):
    form =PostModelForm()
    if request.method =='POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            content=form.cleaned_data['content']
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('dashboard')
    context ={
        'form':form
    }
    return render(request,'create_blogs.html',context)



# @login_required(login_url='login')
def blog(request,pk):
    blog=PostModel.objects.get(id=pk)
    context={'blogs':blog}
    return render(request,'blogpage.html',context)





def create_cmt(request,pk):
    form=CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid(commit=False):
            form.instance.post_id =pk
            form.instance.host=request.user
            form.save()
            return redirect(f'blog/{pk}')
    context ={'form':form}
    return render(request,'comment_form.html',context)


def edit_cmt(request,pk,pk1):
    comment=comments.objects.get(id =pk)
    form=CommentForm(instance=comment)
    if request.method=='POST':
        form=CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.instance.blog_id =pk1
            form.instance.host =request.user
            form.save()
            return redirect(f'/blog/{pk1}')
    context={'form':form}
    return render(request,'comment_form',context)


def delete_cmt(request,pk,pk1):
    comment=comments.objects.get(id=pk)
    comment.delete()
    return redirect(f'/chat/{pk1}')


def create_tag(request):
    form=TagForm()
    if request.method=='POST':
        form=TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
    context ={'form':form}
    return render(request,'newtag.html',context)


