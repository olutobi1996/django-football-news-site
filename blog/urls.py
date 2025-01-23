from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('search/', views.post_search, name='post_search'),  
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('edit_comment/<slug:slug>/<int:comment_id>/', views.comment_edit, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.comment_delete_without_slug, name='comment_delete_without_slug'),
]