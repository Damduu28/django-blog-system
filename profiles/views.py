from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from users.models import User
from blog.models import Topic, Post, Comment

from .forms import PostCreateForm, ProfileUpdateForm

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    posts = user.post_set.all()
    publish_posts = user.post_set.filter(publish=True)
    topics = Topic.objects.all()
    context = {"user": user,
               "posts": posts,
               "topics": topics,
               "publish_posts": publish_posts}
    return render(request, "profiles/user_profile.html", context)

@login_required(login_url="login")
def updateProfile(request, pk):
    user = User.objects.get(id=pk)
    if request.user != user:
        return redirect('home')
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)
    else:
        form = ProfileUpdateForm(instance=user)
    context = {"form": form}
    return render(request, "profiles/update_profile.html", context)
    

@login_required(login_url="login")
def createPost(request):
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        publish = bool(request.POST.get('publish'))
        Post.objects.create(
            host=request.user,
            topic=topic,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            publish=publish,
        )
        return redirect('user-profile', request.user.id)
    else:
        form = PostCreateForm()
        
    topics = Topic.objects.all()
    context = {"form": form, "form_title": "Create Post Form","topics": topics}
    return render(request, "profiles/post_form.html", context)
    
@login_required(login_url="login")
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    
    if request.user != post.host:
        return redirect("home")
    
    if request.method == "POST":
        form = PostCreateForm(request.POST, instance=post)
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        if form.is_valid():
            up_post = form.save(commit=False)
            up_post.topic = topic
            up_post.save()
        return redirect('user-profile', request.user.id)
    else:
        form = PostCreateForm(instance=post)
    context = {"form": form, "post": post}
    return render(request, "profiles/post_form.html", context)

@login_required(login_url="login")
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.user != post.host:
        return redirect('home')
    post.delete()
    return redirect('user-profile', request.user.id)
    
@login_required(login_url="login")
def publishPost(request, pk, post_id):
    user = User.objects.get(id=pk)
    post = Post.objects.get(id=post_id)
    
    if request.user != post.host:
        return redirect('home')
    
    if post.publish == True:
        post.publish = False
    else:
        post.publish = True
    post.save()
    return redirect('user-profile', pk=user.id)




    
    
