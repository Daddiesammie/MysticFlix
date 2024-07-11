from django.shortcuts import render
from movie_media.models import Movie
from blog.models import Post
from blog.models import Comment
from django.http import JsonResponse


def home(request):
    movies = Movie.objects.all()
    latest_posts = Post.objects.order_by('-created_at')[:5]
    random_comments = Comment.objects.order_by('?')[:5]


    context = {'movies': movies, 'latest_posts': latest_posts,'random_comments': random_comments,}
    return render(request, 'home.html', context)

def load_more_comments(request):
    # Retrieve all comments (for "view more" functionality)
    all_comments = Comment.objects.all()

    comments_list = []
    for comment in all_comments:
        comments_list.append({
            'id': comment.id,
            'author': comment.author.username,
            'content': comment.content,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        })

    return JsonResponse({'comments': comments_list})
