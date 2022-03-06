from django.shortcuts import render,redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.

def blog_home(request):
    blogs=Blog.objects.all()

    return render (request,'blog/blog.html',{'blogs':blogs})

def write_blog(request):
    if request.method=="POST":
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
        else:
            print(form.errors)
    else:
        form=BlogForm()
    return render(request,"blog/write_blog.html",{"form":form})