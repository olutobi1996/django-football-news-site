from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post, PostComment
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'This needs approval'
        )
    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )



def comment_edit(request, slug, comment_id):
    comment_post = get_object_or_404(PostComment, pk=comment_id)
    comment_form = CommentForm(data=request.POST, instance=comment)

    if request.method == "POST":

        form = SuggestionCommentForm(request.POST, instance=commentObj)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            new_comment.suggestion = self.get_object()
            new_comment.save()
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            html = render_to_string('suggestion_comments.html', context, request=self.request)
            return JsonResponse({'form': html})
        else:
            form_errors = form.errors.as_json()
            response = HttpResponse(form_errors, status=400)
            response['content_type'] = 'application/json'
            return response

     