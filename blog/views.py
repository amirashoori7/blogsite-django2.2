from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
#from django.views.generic import ListView
from .forms import EmailContactForm, CommentForm
from django.core.mail import send_mail
from taggit.models import Tag

'''
class IndexView(ListView):
    queryset = Post.published.all()
    tags = Post.tags.all()
    context_object_name = 'posts'
    paginate_by = 8
    template_name = 'blog/index.html'
'''

def index(request, tag_slug=None):
    object_list = Post.published.all()
    tags = Post.tags.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = Tag.objects.all()
    paginator = Paginator(object_list, 8)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/index.html',
                   {'page': page, 'posts': posts, 'tag':tag, 'tags':tags})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')

    #List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create a comment object but don't save to db yet
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.post = post
            # save the comment to the db
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  'blog/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})

def contact_us(request):
    if request.method == 'POST':
        form = EmailContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['message']
            message = "{0} has sent you a new message:\n\n{1}".format(name, msg)
            send_mail(subject, message, email, ['a.ashoori7@gmail.com'])
            sent = True
    else:
        form = EmailContactForm()
    return render(request, 'blog/contact.html', {'form':form})
