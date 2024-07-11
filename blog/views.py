from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from .models import Post, Comment, Like

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    is_liked = post.likes.filter(user=request.user).exists()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', post_id=post.id)
    else:
        form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form, 'is_liked': is_liked})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'latest_posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('blog:post_detail', pk=pk)

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            # Update comments queryset after saving new comment
            comments = post.comments.all()
            return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})
    else:
        form = CommentForm()
    
    # Fetch comments for the post before adding a new comment
    comments = post.comments.all()
    
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def blog_page(request):
    latest_posts = Post.objects.order_by('-created_at')[:5]
    random_comments = Comment.objects.order_by('?')[:5]


    context = {'latest_posts': latest_posts,'random_comments': random_comments,}
    return render(request, 'home.html', context)
   