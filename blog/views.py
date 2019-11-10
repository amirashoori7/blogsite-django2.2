from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.views.generic import ListView
from .contact import EmailContactForm
from django.core.mail import send_mail

class IndexView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 8
    template_name = 'blog/index.html'

"""
def index(request):
    object_list = Post.published.all()
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
                   {'page': page, 'posts': posts})
"""

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request,
                  'blog/detail.html', {'post': post})

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
