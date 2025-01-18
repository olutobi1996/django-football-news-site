from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, PostComment
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=0)  # Assuming status=0 is 'Published'
    comments = post.comments.all().order_by("-created_on")  # Now this works
    comment_count = comments.count()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    })

def comment_edit(request, slug, comment_id):
    comment_post = get_object_or_404(PostComment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment_post)
        if comment_form.is_valid() and comment_post.author == request.user:
            comment_form.save()
            messages.success(request, 'Comment Updated!')
        else:
            messages.error(request, 'Error updating comment!')
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug, status=0)  # Assuming status=0 is 'published'
    comment = get_object_or_404(PostComment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))