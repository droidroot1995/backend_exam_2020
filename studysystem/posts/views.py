from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from users.models import User, Student
from posts.models import Post, Comment
from django.shortcuts import get_object_or_404

def posts_list(request, user_id):
    if request.method == "GET":
        user = get_object_or_404(User, id=user_id)
        posts = Post.objects.all().values('topic', 'author', 'content', 'added_at')
        if (user.is_teacher) {
            return JsonResponse({'posts': list(posts)})
        }
        student_class = Student.objects.filter(user=user_id).values('class_name')
        posts = Post.objects.filter(for_class=student_class).values('topic', 'author', 'content', 'added_at')
        return JsonResponse({'posts': list(posts)})
    return HttpResponseNotAllowed(['GET'])

def comments_list(request, post_id):
    if request.method == "GET":
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post_id)
        return JsonResponse({'comments' : list(comments_id)})
    return HttpResponseNotAllowed(['GET'])

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return JsonResponse({'status': 'success!'})
        return JsonResponse({'errors' : form.errors})
    return HttpResponseNotAllowed(['POST'])

def create_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return JsonResponse({'status': 'success!'})
        return JsonResponse({'errors' : form.errors})
    return HttpResponseNotAllowed(['POST'])
