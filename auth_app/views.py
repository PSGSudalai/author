from functools import cache
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.db.models import Q
from django.contrib.auth import login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from auth_app.models import  PostModel, Tags, comments
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
    tags= Tags.objects.filter()
    posts = PostModel.objects.filter((Q(title__icontains=searching)|Q(tags__tags__icontains=searching))).distinct()
    return render(request, 'dashboard.html', {'posts': posts,'tags':tags})



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
    comment =comments.objects.filter(blog=blog)
    context={'blog':blog,'comment':comment}
    return render(request,'blogpage.html',context)




def create_cmt(request, pk):
    blog = get_object_or_404(PostModel, pk=pk)
    if request.method == 'POST':
        comment_text = request.POST.get("comment")
        if comment_text:
            comments.objects.create(
                text=comment_text,
                host=request.user,
                blog=blog
            )
        return redirect('blog', pk=blog.id)
    else:
        form = CommentForm()
    
    return render(request, 'comment_form.html', {'form': form, 'blog': blog})


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
    return render(request,'comment_form.html',context)


def delete_cmt(request,pk,pk1):
    comment=comments.objects.get(id=pk)
    comment.delete()
    return redirect(f'/blog/{pk1}')



def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')  
    else:
        form = TagForm()

    context = {'form': form}
    return render(request, 'newtag.html', context)


def edit(request, pk):
    blog = get_object_or_404(PostModel, id=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=blog)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.host = request.user
            new_blog.save()
            return redirect('dashboard')
    else:
        form = PostModelForm(instance=blog)
    
    context = {
        'form': form,
        'blog': blog
    }
    return render(request, 'create_blogs.html', context)

def delete(request,pk):
    blog=PostModel.objects.get(id=pk)
    blog.delete()
    return redirect('dashboard')