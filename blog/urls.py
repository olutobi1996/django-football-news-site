from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('search/', views.post_search, name='post_search'),  
    path('edit_comment/<slug:slug>/<int:comment_id>/', views.comment_edit, name='edit_comment'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
]