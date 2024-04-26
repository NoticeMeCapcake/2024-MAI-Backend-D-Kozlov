import json

from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from blog.models import UserPost, Comment, UserProfile, Like


@csrf_exempt
@require_http_methods(['GET'])
def all_posts(request):
    posts = UserPost.objects.all()
    context = {'posts': [model_to_dict(post) for post in posts]}
    return JsonResponse(context)


@csrf_exempt
@require_http_methods(['GET'])
def all_comments(request, post_id):
    comments = Comment.objects.filter(post_id=post_id)
    context = {'comments': [model_to_dict(comment) for comment in comments]}
    return JsonResponse(context)


@csrf_exempt
@require_http_methods(['GET'])
def all_users(request):
    users = UserProfile.objects.all()
    context = {'users': [model_to_dict(user) for user in users]}
    return JsonResponse(context)


@csrf_exempt
@require_http_methods(['POST'])
def create_post(request, author_id=None):
    if author_id is None:
        return HttpResponseBadRequest({'status': 'error', 'message': 'author_id is required'})
    data = json.loads(request.body)['user']
    try:
        author = UserProfile.objects.get(pk=author_id)
    except UserProfile.DoesNotExist as ex:
        return HttpResponseBadRequest({'status': 'error', 'message': ex})
    UserPost.objects.create(author_id=author, content=data['content'], title=data['title'])
    return JsonResponse({'status': 'ok'})


@csrf_exempt
@require_http_methods(['POST'])
def create_user(request):
    data = json.loads(request.body)['user']
    UserProfile.objects.create(login=data['login'], password=data['password'])
    return JsonResponse({'status': 'ok'})


@csrf_exempt
@require_http_methods(['POST'])
def create_comment(request, author_id=None, post_id=None):
    if author_id is None or post_id is None:
        return HttpResponseBadRequest({'status': 'error', 'error': 'author_id and post_id are required'})
    try:
        author = UserProfile.objects.get(pk=author_id)
        post = UserPost.objects.get(pk=post_id)
    except UserProfile.DoesNotExist or UserProfile.DoesNotExist as ex:
        return HttpResponseBadRequest({'status': 'error', 'error': ex})
    new_comment = json.loads(request.body)['comment']
    Comment.objects.create(author_id=author, post_id=post, content=new_comment['content'])
    return JsonResponse({'status': 'ok'})


@csrf_exempt
@require_http_methods(['GET', 'DELETE', 'POST'])
def single_post(request, post_id=None, author_id=None):
    try:
        if request.method == 'GET':
            if post_id is None:
                return HttpResponseBadRequest({'status': 'error', 'error': 'post_id is required'})
            post = UserPost.objects.get(pk=post_id)
            context = {'post': model_to_dict(post)}
            return JsonResponse(context)

        elif request.method == 'DELETE':
            if post_id is None:
                return HttpResponseBadRequest({'status': 'error', 'error': 'post_id is required'})
            UserPost.objects.get(pk=post_id).delete()
            return JsonResponse({'status': 'ok'})

        elif request.method == 'POST':
            if author_id is None:
                return HttpResponseBadRequest({'status': 'error', 'error': 'author_id is required'})
            author = UserProfile.objects.get(pk=author_id)
            new_post = json.loads(request.body)['post']  # dict of content, title
            UserPost.objects.create(author_id=author, content=new_post['content'], title=new_post['title'])
            return JsonResponse({'status': 'ok'})
    except UserPost.DoesNotExist or UserProfile.DoesNotExist as ex:
        return HttpResponseBadRequest({'status': 'error', 'error': ex})


@csrf_exempt
@require_http_methods(['GET', 'DELETE', 'POST'])
def single_user(request, user_id=None):
    try:
        if request.method == 'GET':
            if user_id is None:
                return HttpResponseBadRequest({'status': 'error', 'error': 'user_id is required'})
            try:
                user = UserProfile.objects.get(pk=user_id)
            except UserProfile.DoesNotExist as ex:
                return HttpResponseBadRequest({'status': 'error', 'error': ex})
            context = {'user': model_to_dict(user)}
            return JsonResponse(context)

        elif request.method == 'DELETE':
            if user_id is None:
                return HttpResponseBadRequest({'status': 'error', 'error': 'user_id is required'})
            UserProfile.objects.get(pk=user_id).delete()
            return JsonResponse({'status': 'ok'})

        elif request.method == 'POST':
            data = json.loads(request.body)['user']
            UserProfile.objects.create(login=data['login'], password=data['password'])
            return JsonResponse({'status': 'ok'})
    except UserProfile.DoesNotExist as ex:
        return HttpResponseBadRequest({'status': 'error', 'error': ex})


@csrf_exempt
@require_http_methods(['POST', 'DELETE'])
def single_comment(request, post_id=None, author_id=None, comment_id=None):
    try:
        if request.method == "POST":
            if author_id is None or post_id is None:
                return HttpResponseBadRequest({'status': 'error', 'error': 'author_id and post_id are required'})
            author = UserProfile.objects.get(pk=author_id)
            post = UserPost.objects.get(pk=post_id)
            new_comment = json.loads(request.body)['comment']
            Comment.objects.create(author_id=author, post_id=post, content=new_comment['content'])
            return JsonResponse({'status': 'ok'})

        elif request.method == "DELETE":
            if comment_id is None:
                return HttpResponseBadRequest({'status': 'error', 'error': 'comment_id is required'})
            UserPost.objects.get(pk=comment_id).delete()
            return JsonResponse({'status': 'ok'})
    except UserPost.DoesNotExist or UserProfile.DoesNotExist as ex:
        return HttpResponseBadRequest({'status': 'error', 'error': ex})


@csrf_exempt
@require_http_methods(['POST', 'DELETE'])
def user_like(request, post_id: int, author_id: int):
    if post_id is None or author_id is None:
        return HttpResponseBadRequest({'status': 'error', 'error': 'post_id and author_id is required'})
    try:
        user = UserProfile.objects.get(pk=author_id)
        post = UserPost.objects.get(pk=post_id)
    except UserProfile.DoesNotExist or UserPost.DoesNotExist as ex:
        return HttpResponseBadRequest({'status': 'error', 'error': ex})

    if request.method == "POST":
        try:
            Like.objects.create(author_id=user, post_id=post)
        except Exception as ex:
            return HttpResponseBadRequest({'status': 'error', 'error': ex})
        return JsonResponse({'status': 'ok'})

    elif request.method == "DELETE":
        try:
            Like.objects.get(author_id=user, post_id=post).delete()
        except Like.DoesNotExist as ex:
            return HttpResponseBadRequest({'status': 'error', 'error': ex})
        return JsonResponse({'status': 'ok'})


@csrf_exempt
@require_http_methods(['GET'])
def search_posts(request, query=None):
    if query is None or query.isspace() or query == '':
        posts = UserPost.objects.all()
    else:
        posts = UserPost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

    context = {'posts': [model_to_dict(post) for post in posts]}
    return JsonResponse(context)
