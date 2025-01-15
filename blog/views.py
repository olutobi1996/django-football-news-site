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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.postcomment_set.all().order_by("-created_on")
    comment_count = post.postcomment_set.count()
    comments = post.comments.filter(approve=True)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'This needs approval'
        )
    comment_form = CommentForm()

    print('COMMENTS: ', comments)

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
        },
    )
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