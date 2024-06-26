from django.urls import path

from blog import views

urlpatterns = [
    path('posts/', views.all_posts, name='all_posts'),
    path(
        'post/post_id=<int:post_id>&author_id<int:author_id>',
        views.single_post,
        name='single_post_with_id_author'
    ),
    path('post/post_id=<int:post_id>', views.single_post, name='single_post_with_id'),
    path('post/author_id=<int:author_id>', views.single_post, name='single_post_with_author'),
    path('post/create/author_id=<int:author_id>', views.create_post, name='create_post_with_author'),
    path('users/', views.all_users, name='all_users'),
    path('user/user_id=<int:user_id>', views.single_user, name='single_user_with_id'),
    path('user/', views.single_user, name='single_user'),
    path('user/create', views.create_user, name='create_user'),
    path('comments/post_id=<int:post_id>', views.all_comments, name='all_comments'),
    path(
        'comment/post_id=<int:post_id>&author_id=<int:author_id>',
        views.single_comment,
        name='single_comment_with_post_author'
    ),
    path(
        'comment/create/post_id=<int:post_id>&author_id=<int:author_id>',
        views.single_comment,
        name='create_comment_with_post_author'
    ),
    path(
        'comment/comment_id<int:comment_id>',
        views.single_comment,
        name='single_comment_with_id'
    ),
    path('posts/search/q=<str:query>', views.search_posts, name='search_posts'),
    path('posts/search/', views.search_posts, name='search_posts'),
]