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

def post_detail(request, comment_id):
    # Get the specific post by its primary key (pk)
    post = get_object_or_404(Post, pk=comment_id)

    # Get only approved comments related to this post
    comments = post.comments.filter(approve=True)

    # Check if the request method is POST (for adding new comments)
    if request.method == 'POST':
        # Assuming you have a CommentForm in forms.py
        from .forms import CommentForm  # Import the form

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Associate the comment with the post
            comment.save()  # Save the comment (it won't be approved by default)
    else:
        form = CommentForm()  # Display an empty form for GET requests

    # Render the template with the post, comments, and form
    return render(request, 'blog/post_detail.html', {
           "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
    })
    
def comment_edit(request, slug, comment_id):
    comment_post = get_object_or_404(PostComment, pk=comment_id)
    comment_form = CommentForm(data=request.POST, instance=comment)

    if request.method == "POST":

        form = SuggestionCommentForm(request.POST, instance=commentObj)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
        

def comment_delete(request, slug, comment_id):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))