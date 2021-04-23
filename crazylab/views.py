from django.views.generic import ListView
from .models import Post, Category, Comment
from users.models import JProfile, Coin, Item
from django.contrib.auth.models import User, Group
from .forms import PublicIdeaPostForm, TodayIdeaPostForm, CrazyIdeaPostForm, QuestionIdeaPostForm, IssueIdeaPostForm, SystemIdeaPostForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count


class PublicIdeaListView(ListView):
    model = Post
    template_name = 'crazylab/publicidea_list.html'
    context_object_name = 'posts'
    paginate_by = 47

    def get_queryset(self):
        return Post.objects.filter(category__name='공익아이디어').select_related('author').prefetch_related(
            'author__profile').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(PublicIdeaListView, self).get_context_data(**kwargs)
        context['tops'] = Post.objects.filter(category__name='공익아이디어').annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:5]

        return context


class TodayIdeaListView(ListView):
    model = Post
    template_name = 'crazylab/todayidea_list.html'
    context_object_name = 'posts'
    paginate_by = 47

    def get_queryset(self):
        return Post.objects.filter(category__name='오늘의아이디어').select_related('author').prefetch_related(
            'author__profile').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(TodayIdeaListView, self).get_context_data(**kwargs)
        context['tops'] = Post.objects.filter(category__name='오늘의아이디어').annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:5]

        return context


class CrazyIdeaListView(ListView):
    model = Post
    template_name = 'crazylab/crazyidea_list.html'
    context_object_name = 'posts'
    paginate_by = 47

    def get_queryset(self):
        return Post.objects.filter(category__name='크레이지아이디어').select_related('author').prefetch_related(
            'author__profile').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(CrazyIdeaListView, self).get_context_data(**kwargs)
        context['tops'] = Post.objects.filter(category__name='크레이지아이디어').annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:5]

        return context


def post_crazyidea(request):
    if request.method == "POST":
        form =  CrazyIdeaPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category =  Category.objects.get(name='크레이지아이디어')
            post.save()
            coin = Coin.objects.only('blackcoin').get(user=request.user)
            coin.blackcoin += 1
            coin.save()
            return HttpResponseRedirect(reverse('crazylab:crazyidea_list'))
    else:
        form =  CrazyIdeaPostForm()

    context = {
        'form' : form,
    }
    return render(request, 'crazylab/crazyidea_post.html', context)


@login_required(login_url='login')
def crazylab_detail(request, pk):
    post = Post.objects.select_related('author','author__profile').prefetch_related('scrap').get(pk=pk)

    comments = Comment.objects.select_related('author', 'author__profile').prefetch_related(
                'up', 'replies__up', 'replies__author__profile').filter(post=post, reply=None)

    comment_all = Comment.objects.filter(post=post)

    comment_top = Comment.objects.select_related('author','author__profile').prefetch_related(
                'up').filter(post=post).order_by('-total','-created_date')[:3]

    jprofile = JProfile.objects.values('department').get(user=request.user)

    if request.method =='POST':
        contents = request.POST.get('contents')
        reply_id = request.POST.get('comment_id')
        comment_qs = None
        if reply_id:
            comment_qs = Comment.objects.get(id=reply_id)
        comment = Comment.objects.create(post=post, author=request.user, contents=contents, reply=comment_qs)
        comment.save()

    context = {
        'post' : post,
        'comments' : comments,
        'comment_all' : comment_all,
        'comment_top' : comment_top,
        'get_total_scrap' : post.get_total_scrap(),
        'get_total_star' : post.get_total_star(),
        'jprofile' : jprofile
    }

    if request.is_ajax():
        html = render_to_string('crazylab/section/comments.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'crazylab/crazylab_detail.html', context)


@login_required(login_url='login')
def post_publicidea(request):
    if request.method == "POST":
        form =  PublicIdeaPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category =  Category.objects.get(name='공익아이디어')
            post.save()
            coin = Coin.objects.only('blackcoin').get(user=request.user)
            coin.blackcoin += 1
            coin.save()
            return HttpResponseRedirect(reverse('crazylab:publicidea_list'))
    else:
        form =  PublicIdeaPostForm()

    context = {
        'form' : form,
    }
    return render(request, 'crazylab/publicidea_post.html', context)


def post_todayidea(request):
    if request.method == "POST":
        form =  TodayIdeaPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category =  Category.objects.get(name='오늘의아이디어')
            post.save()
            coin = Coin.objects.only('blackcoin').get(user=request.user)
            coin.blackcoin += 1
            coin.save()
            return HttpResponseRedirect(reverse('crazylab:todayidea_list'))
    else:
        form =  TodayIdeaPostForm()

    context = {
        'form' : form,
    }
    return render(request, 'crazylab/todayidea_post.html', context)


def recommend(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    if post.author != request.user:
        if post.recommend.filter(id=request.user.id).exists():
            messages.info(request, "이미 추천하였습니다.")
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
        html = render_to_string('crazylab/section/recommend_section.html', context, request=request)
    return JsonResponse({'form': html})


def add_star(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    item = Item.objects.get(user=request.user)
    if post.author != request.user:
        if post.star.filter(id=request.user.id).exists():
            msg = "별을 이미 사용하였습니다."
        else:
            if item.star >= 1:
                post.star.add(request.user)
                post.all_recommend += 5
                post.save()
                item.star -= 1
                item.save()
            else:
                msg = "별이 없습니다."
    else:
        msg = "불가능 합니다."

    context = {
        'post' : post,
        'msg' : msg,
        'get_total_star' : post.get_total_star()
    }
    if request.is_ajax():
        html = render_to_string('crazylab/section/star_section.html', context, request=request)
        html2 = render_to_string('crazylab/section/recommend_section.html', {'post':post}, request=request)
    return JsonResponse({'form': html, 'form2': html2})


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
        html = render_to_string('crazylab/section/scrap_section.html' , context, request=request)
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
            html = render_to_string('crazylab/section/comment_up_section.html', context, request=request)
        elif kind == 'reply':
            html = render_to_string('crazylab/section/reply_up_section.html', context, request=request)
        elif kind == 'top':
            html = render_to_string('crazylab/section/top_up_section.html', context, request=request)
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
        html = render_to_string('crazylab/section/post_accuse_section.html', request=request)
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
            html = render_to_string('crazylab/section/comment_accuse_section.html', request=request)
        elif kind == 'reply':
            html = render_to_string('crazylab/section/reply_accuse_section.html', request=request)
        elif kind == 'top':
            html = render_to_string('crazylab/section/top_accuse_section.html', request=request)
    return JsonResponse({'form': html})
