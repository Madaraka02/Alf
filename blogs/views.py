from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages

# Create your views here.
def blogs(request):
    blogs=Blog.objects.filter(approved=True).order_by('-id')
    context ={
        'blogs':blogs
    }
    return render(request, 'blog.html',context)


def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    form = BlogForm(instance=blog) 
    if request.method == "POST":

        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Your blog was updated successfully")
            return redirect('user_profile')
    context = {
        'blog':blog,
        'form':form,
    }
    return render(request, 'form.html', context)    
    
def postblog(request):
    if request.user.is_authenticated:
        form = BlogForm() 
        if request.method == "POST":
            form = BlogForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                blog = form.save(commit=False)   
                blog.author = request.user
                blog.save()
                messages.success(request, "Your blog was added")
                return redirect('user_profile')
    
        context = {
            'form':form,
        }
        return render(request, 'add.html', context)

def delete_blog(request, id):
    blog = get_object_or_404(Blog, id = id)
    blog.delete()
    messages.success(request, "Your blog was deleted successfully")
    return redirect('user_profile')



class LikeBlog(generic.View):
    def post(self, request, id ,*args, **kwargs):
        blog= get_object_or_404(Blog, id=id)

        is_disliked=False

        for dislike in blog.dislikes.all():
            if dislike == request.user:
                is_disliked=True
                break

        if is_disliked:
            blog.dislikes.remove(request.user)   

        is_liked=False

        for like in blog.likes.all():
            if like == request.user:
                is_liked=True
                break
        if not is_liked:
            blog.likes.add(request.user)

        if is_liked:
            blog.likes.remove(request.user)   

        next=request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class DislikeBlog(generic.View):
    def post(self, request, id ,*args, **kwargs):
        blog= get_object_or_404(Blog, id=id)

        is_liked=False

        for like in blog.likes.all():
            if like == request.user:
                is_liked=True
                break

        if is_liked:
            blog.likes.remove(request.user) 

        is_disliked=False

        for dislike in blog.dislikes.all():
            if dislike == request.user:
                is_disliked=True
                break
        if not is_disliked:
            blog.dislikes.add(request.user)

        if is_disliked:
            blog.dislikes.remove(request.user)   


        next=request.POST.get('next', '/')
        return HttpResponseRedirect(next)



# urls
# 

class BlogComment(generic.View):

    def post(self, request, pk ,*args, **kwargs):
        blog= get_object_or_404(Blog, id=pk) 

        comment=request.POST.get('comment')
        comm = Comment.objects.create(author=request.user, comment=comment, blog=blog)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog=blog
            comment.author=request.user
            comment.save()

        context={
            'blog':blog,
        }

        return render(request, 'blog.html', context)    
   

def blog_comment(request):
    if request.method =='POST':
        comment = request.POST['comment']
        blogID = request.POST['blog']
        user=request.user
        blog=get_object_or_404(Blog, id=blogID)

        Comment.objects.create(
            blog=blog,
            author=user,
            comment=comment,
        )

    return JsonResponse({'bool':True})


def approve_blog(request, id):
    blog= get_object_or_404(Blog, id=id)
    if blog.approved == False:
        blog.approved=True
        blog.save()
        messages.success(request, "Blog was approved ")

        return redirect('admin_blogs')


def book(request):
    return render(request, 'booking.html')