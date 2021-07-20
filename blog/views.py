from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.db.models import Count,Q
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, PostForm,CategoryForm
from django.contrib.admin.views.decorators import staff_member_required


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def get_category_count():
    qs = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return qs

@login_required
def index(request):
    template = 'myblog/index.html'
    most_recent_post = Post.objects.order_by('-timestamp')[:5]
    context = {
        'most_recent_post':most_recent_post
    }
    return render(request, template, context)

@login_required
def post_list(request):
    # login
    post_create_form = PostForm(request.POST or None)
    post_list = Post.objects.order_by('-timestamp')
    paginator = Paginator(post_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)

    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)
    # rpv = requst page variable
    most_recent_post = Post.objects.order_by('-timestamp')[:5]  
    context = {
        'post_form': post_create_form,
        'post_list': paginated_qs,
        'rpv': page_request_var,
        'most_recent_post': most_recent_post,
    }
    return render(request, 'myblog/blog.html', context)

@login_required
def post_detail(request, id):

    post = get_object_or_404(Post, id=id)
    #caregory count
    category_count = get_category_count()
    PostView.objects.get_or_create(user=request.user, post=post)
        # comment
    comments = Comment.objects.all()
    commentform = CommentForm(request.POST or None)
    if request.method == 'POST':
        if commentform.is_valid():
            commentform.instance.user = request.user
            commentform.instance.post = post
            commentform.save()
            return redirect(reverse('blog:post_detail' ,kwargs={'id':post.id}))
    most_recent_post = Post.objects.order_by('-timestamp')[:5]
    context = {
        'post': post,
        'category_count': category_count,
        'most_recent_post': most_recent_post,
        'commentform': commentform,
        # 'form':loginform,
    }
    return render(request, 'myblog/post_detail.html', context)


@staff_member_required
def post_update(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    post_to_update = get_object_or_404(Post, id=id)
    author = get_author(request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post_to_update)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('blog:post_detail', kwargs={'id': form.instance.id}))
    context = {
        'updt_form': form,
        'post':post_to_update,

    }
    return render(request,'myblog/post_update.html', context)

@staff_member_required
def post_delete(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    post_to_delete = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post_to_delete.delete()
        return redirect(reverse('blog:post_list'))
    return redirect(reverse('blog:post_list'))


@staff_member_required
def post_create(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    author = get_author(request.user)
    post_form = PostForm(request.POST or None,request.FILES or None)
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.instance.author = author
            post_form.save()
            return redirect(reverse('blog:post_detail', kwargs={'id': post_form.instance.id}))
    context = {
        'postForm':post_form
    }
    return render(request, 'myblog/createBlog.html', context)

@staff_member_required
def createCat(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    categories = Category.objects.all()
    form = CategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:createCat'))
    context = {
        'form':form,
        'categories':categories
    }
    return render(request, 'myblog/createCat.html', context)

@login_required
def search(request):
    qs = Post.objects.all()
    q = request.GET.get('q')
    if q:
        qs = qs.filter(
            Q(title__icontains=q) |
            Q(overview__icontains=q)
        ).distinct()
    most_recent_post = Post.objects.order_by('-timestamp')[:5]
    context = {
        'results': qs,
        'q':q,
        'most_recent_post': most_recent_post,
    }
    return render(request, 'myblog/search_results.html', context)
