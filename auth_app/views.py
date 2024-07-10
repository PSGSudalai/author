from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login,logout
from django.urls import reverse
from auth_app.models import PostModel
from .form import PostModelForm

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
    posts =PostModel.objects.all()
    if request.method =='POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('dashboard')
    else:
        form =PostModelForm()
    context ={
        'posts':posts,
        'form':form
    }
    return render(request,'dashboard.html',context)

def get_absolute_url(self):
        return reverse('blog', args=[str(self.pk)])
class Meta:
        ordering = ['-last_updated','-created']


def search(request):
    search_obj=request.GET.get('search')
    result=PostModel.objects.filter(title=search_obj)
    return render