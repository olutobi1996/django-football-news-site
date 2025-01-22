from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, PostComment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6

 # comment form
@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1) 
    comments = post.comments.all().order_by("-created_on")
    comment_count = comments.count()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user  # Set the user here
            comment.save()
            messages.success(request, 'Comment added successfully!')
        else:
            messages.error(request, 'There was an error adding your comment.')
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    })

@login_required
def comment_edit(request, slug, comment_id):
    comment = get_object_or_404(PostComment, pk=comment_id)
    # Ensure only the owner can edit
    if comment.user != request.user:
        messages.error(request, "You are not authorized to edit this comment.")
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully!')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(request, 'Error updating comment.')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'post': comment.post})



def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug, status=0)  # Assuming status=0 is 'published'
    comment = get_object_or_404(PostComment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def post_search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query),
        status=1  # Assuming 1 is "Published"
    ) if query else Post.objects.none()

    return render(request, 'blog/search_results.html', {'query': query, 'results': results})
    