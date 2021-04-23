from django.views.generic import ListView
from .models import Post, Category, Comment
from django.contrib.auth.models import User
from users.models import Coin, Item
from .forms import NovelPostForm, PoetryPostForm, LetterPostForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages


class NovelListView(ListView):
    model = Post
    template_name = 'reality/novel_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='소설').select_related('author').prefetch_related(
            'author__profile').only('title', 'all_recommend', 'author','date_posted')

    def get_context_data(self, **kwargs):
        context = super(NovelListView, self).get_context_data(**kwargs)
        context['tops'] = Post.objects.filter(category__name='소설').only(
            'title', 'contents', 'all_recommend').order_by('-all_recommend','-date_posted')[:3]

        return context


class PoetryListView(ListView):
    model = Post
    template_name = 'reality/poetry_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='시').select_related('author').prefetch_related(
            'author__profile').only('title', 'all_recommend', 'author','date_posted')

    def get_context_data(self, **kwargs):
        context = super(PoetryListView, self).get_context_data(**kwargs)
        context['tops'] = Post.objects.filter(category__name='시').only(
            'title', 'contents', 'all_recommend').order_by('-all_recommend','-date_posted')[:3]

        return context


class LetterListView(ListView):
    model = Post
    template_name = 'reality/letter_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='편지').select_related('author').prefetch_related(
            'author__profile').only('title', 'all_recommend', 'author','date_posted')

    def get_context_data(self, **kwargs):
        context = super(LetterListView, self).get_context_data(**kwargs)
        context['tops'] = Post.objects.filter(category__name='편지').only(
            'title', 'contents', 'all_recommend').order_by('-all_recommend','-date_posted')[:3]

        return context


def reality_detail(request, pk):
    post = Post.objects.select_related('author','author__profile').prefetch_related('recommend','scrap').get(pk=pk)

    comments = Comment.objects.select_related('author', 'author__profile').prefetch_related(
                'up', 'replies__up', 'replies__author__profile').filter(post=post, reply=None)

    comment_all = Comment.objects.filter(post=post)

    comment_top = Comment.objects.select_related('author','author__profile').prefetch_related(
                'up').filter(post=post).order_by('-total','-created_date')[:3]

    if request.method =='POST':
        contents = request.POST.get('contents')
        reply_id = request.POST.get('comment_id')
        comment_qs = None
        if reply_id:
            comment_qs = Comment.objects.get(id=reply_id)
        comment = Comment.objects.create(post=post, author=request.user, contents=contents, reply=comment_qs)
        comment.save()

    context = {
        'post': post,
        'comments': comments,
        'comment_all' : comment_all,
        'comment_top' : comment_top,
        'get_total_scrap' : post.get_total_scrap(),
    }

    if request.is_ajax():
        html = render_to_string('reality/section/comments.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'reality/reality_detail.html', context)


@login_required(login_url='login')
def post_novel(request):
    if request.method == "POST":
        form = NovelPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category =  Category.objects.get(name='소설')
            post.save()
            coin = Coin.objects.only('blackcoin').get(user=request.user)
            coin.blackcoin += 1
            coin.save()
            return HttpResponseRedirect(reverse('reality:novel_list'))
    else:
        form = NovelPostForm()

    context = {
        'form' : form,
    }
    return render(request, 'reality/novel_post.html', context)


@login_required(login_url='login')
def post_poetry(request):
    if request.method == "POST":
        form = PoetryPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category =  Category.objects.get(name='시')
            post.save()
            coin = Coin.objects.only('blackcoin').get(user=request.user)
            coin.blackcoin += 1
            coin.save()
            return HttpResponseRedirect(reverse('reality:poetry_list'))
    else:
        form = PoetryPostForm()

    context = {'form' : form}
    return render(request, 'reality/poetry_post.html', context)


@login_required(login_url='login')
def post_letter(request):
    item = get_object_or_404(Item, user=request.user)
    if request.method == "POST":
        form = LetterPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category =  Category.objects.get(name='편지')
            post.save()
            coin = Coin.objects.only('blackcoin').get(user=request.user)
            coin.blackcoin += 1
            coin.save()
            item.letter -= 1
            item.save()
            return HttpResponseRedirect(reverse('reality:letter_list'))
    else:
        if request.user.item.letter >= 1:
            form = LetterPostForm()
        else:
            messages.info(request, "편지 작성권이 없습니다.")
            return HttpResponseRedirect(reverse('reality:letter_list'))

    context = {'form' : form}
    return render(request, 'reality/letter_post.html', context)


def recommend(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    if post.author != request.user:
        if post.recommend.filter(id=request.user.id).exists():
            messages.info(request, "이미추천하였습니다.")
        else:
            post.recommend.add(request.user)
            post.all_recommend += 1
            post.save()
    else:
        messages.info(request, "불가능 합니다.")

    context = {
        'post' : post,
    }
    if request.is_ajax():
        html = render_to_string('reality/section/recommend_section.html', context, request=request)
    return JsonResponse({'form': html})


def scrap(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    if post.scrap.filter(id=request.user.id).exists():
        post.scrap.remove(request.user)
        messages.info(request, "스크랩을 취소 하였습니다.")
    else:
        post.scrap.add(request.user)
        messages.info(request, "이 글을 스크랩 하였습니다.")

    context = {
        'post' : post,
        'get_total_scrap' : post.get_total_scrap()
    }
    if request.is_ajax():
        html = render_to_string('reality/section/scrap_section.html' , context, request=request)
    return JsonResponse({'form': html})


def user_scrap(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.scrap.filter(id=request.user.id).exists():
        post.scrap.remove(request.user)

    return redirect(request.META['HTTP_REFERER'])


def up_comment(request):
    comment = get_object_or_404(Comment, id=request.POST.get('id'))
    kind = request.POST.get('kind')
    if comment.author != request.user:
        if comment.up.filter(id=request.user.id).exists():
            messages.info(request, "이미 UP 하였습니다.")
        else:
            comment.up.add(request.user)
            comment.total += 1
            comment.save()
    else:
        messages.info(request, "불가능합니다.")

    if kind == 'comment':
        context = {'comment' : comment}

    elif kind == 'reply':
        reply = comment
        context = {
            'reply' : reply,
        }

    elif kind == 'top':
        top = comment
        context = {
            'top' : top,
        }

    if request.is_ajax():
        if kind == 'comment':
            html = render_to_string('reality/section/comment_up_section.html', context, request=request)
        elif kind == 'reply':
            html = render_to_string('reality/section/reply_up_section.html', context, request=request)
        elif kind == 'top':
            html = render_to_string('reality/section/top_up_section.html', context, request=request)
    return JsonResponse({'form': html})


def accuse_post(request):
    if request.method == 'POST':
        post =get_object_or_404(Post, id=request.POST.get('id'))
        post.accused += 1
        post.save()
        accused = User.objects.get(id=request.POST.get('post_author'))
        accused_item = Item.objects.get(user=accused)
        accused_item.accused += 1
        accused_item.save()
        messages.info(request, "해당 게시글을 신고하였습니다.")
        if post.accused >= 10:
            post.title = '신고가 누적되어 해당 글은 제재되었습니다.'
            post.contents = '신고가 누적되어 해당 글은 제재되었습니다.'
            post.save()

        if accused_item.accused >= 20:
            group = Group.objects.get(name='Accused')
            accused.groups.add(group)
            accused_item.accused = 0
            accused_item.save()

    if request.is_ajax():
        html = render_to_string('reality/section/post_accuse_section.html', request=request)
    return JsonResponse({'form': html})


def accuse_comment(request):
    kind = request.POST.get('kind')
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=request.POST.get('id'))
        comment.accused += 1
        comment.save()
        accused = User.objects.get(id=request.POST.get('comment_author'))
        accused_item = Item.objects.get(user=accused)
        accused_item.accused += 1
        accused_item.save()
        messages.info(request, "신고하였습니다.")
        if comment.accused >= 10:
            comment.delete()

        if accused_item.accused >= 20:
            group = Group.objects.get(name='Accused')
            accused.groups.add(group)
            accused_item.accused = 0
            accused_item.save()

    if request.is_ajax():
        if kind == 'comment':
            html = render_to_string('reality/section/comment_accuse_section.html', request=request)
        elif kind == 'reply':
            html = render_to_string('reality/section/reply_accuse_section.html', request=request)
        elif kind == 'top':
            html = render_to_string('reality/section/top_accuse_section.html', request=request)
    return JsonResponse({'form': html})
