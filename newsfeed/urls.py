# newsfeed/urls.py
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from .views import register
from .views import profile_view


urlpatterns = [
    path('', views.post_list, name='home'),
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('register/', views.register, name='register'),
    path('comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

]

