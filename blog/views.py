from django.shortcuts import render, redirect

# Create your views here.
from .models import Topic, Post, Comment

def home(request):
    posts = Post.objects.filter(publish=True)
    topics = Topic.objects.all()
    context = {"posts": posts, "topics": topics}
    return render(request, "blog/home.html", context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        comment = Comment.objects.create(
            user=request.user,
            post=post,
            body=request.POST.get('body')
        )
        post.participants.add(request.user)
        return redirect('post', slug=post.slug)
    comments = post.comment_set.all()
    participants = post.participants.all()
    context = {'page': 'post',
               'post': post,
               'comments': comments,
               'participants': participants,
               }
    return render(request, "blog/post.html", context)

def deleteComment(request, slug, pk):
    post = Post.objects.get(slug=slug)
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return redirect('post', slug=post.slug)

    
    
