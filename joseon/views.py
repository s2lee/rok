from django.views.generic import ListView
from .models import Post, Category, Comment
from users.models import JProfile, Coin, Item, Ranker
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q, Count
from django.contrib import messages
import random


class PoliticsListView(ListView):
    model = Post
    template_name = 'joseon/politics_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='정치').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(PoliticsListView, self).get_context_data(**kwargs)

        context['progressivism_tops'] = Post.objects.filter(
                category__name='정치', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['centrism_tops'] = Post.objects.filter(
                Q(category__name='정치') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['conservatism_tops'] = Post.objects.filter(
                category__name='정치', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['progressivism_tops_mobile'] = Post.objects.filter(
                category__name='정치', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['centrism_tops_mobile'] = Post.objects.filter(
                Q(category__name='정치') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['conservatism_tops_mobile'] = Post.objects.filter(
                category__name='정치', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        return context


class EconomyListView(ListView):
    model = Post
    template_name = 'joseon/economy_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='경제').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(EconomyListView, self).get_context_data(**kwargs)

        context['progressivism_tops'] = Post.objects.filter(
                category__name='경제', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['centrism_tops'] = Post.objects.filter(
                Q(category__name='경제') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['conservatism_tops'] = Post.objects.filter(
                category__name='경제', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['progressivism_tops_mobile'] = Post.objects.filter(
                category__name='경제', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['centrism_tops_mobile'] = Post.objects.filter(
                Q(category__name='경제') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['conservatism_tops_mobile'] = Post.objects.filter(
                category__name='경제', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        return context


class SocietyListView(ListView):
    model = Post
    template_name = 'joseon/society_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='사회').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(SocietyListView, self).get_context_data(**kwargs)

        context['progressivism_tops'] = Post.objects.filter(
                category__name='사회', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['centrism_tops'] = Post.objects.filter(
                Q(category__name='사회') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['conservatism_tops'] = Post.objects.filter(
                category__name='사회', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['progressivism_tops_mobile'] = Post.objects.filter(
                category__name='사회', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['centrism_tops_mobile'] = Post.objects.filter(
                Q(category__name='사회') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['conservatism_tops_mobile'] = Post.objects.filter(
                category__name='사회', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        return context


class WorldListView(ListView):
    model = Post
    template_name = 'joseon/world_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='세계').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(WorldListView, self).get_context_data(**kwargs)

        context['progressivism_tops'] = Post.objects.filter(
                category__name='세계', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['centrism_tops'] = Post.objects.filter(
                Q(category__name='세계') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['conservatism_tops'] = Post.objects.filter(
                category__name='세계', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['progressivism_tops_mobile'] = Post.objects.filter(
                category__name='세계', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['centrism_tops_mobile'] = Post.objects.filter(
                Q(category__name='세계') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['conservatism_tops_mobile'] = Post.objects.filter(
                category__name='세계', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        return context


class IdeologyListView(ListView):
    model = Post
    template_name = 'joseon/ideology_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='이념').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(IdeologyListView, self).get_context_data(**kwargs)

        context['progressivism_tops'] = Post.objects.filter(
                category__name='이념', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['centrism_tops'] = Post.objects.filter(
                Q(category__name='이념') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['conservatism_tops'] = Post.objects.filter(
                category__name='이념', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['progressivism_tops_mobile'] = Post.objects.filter(
                category__name='이념', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['centrism_tops_mobile'] = Post.objects.filter(
                Q(category__name='이념') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['conservatism_tops_mobile'] = Post.objects.filter(
                category__name='이념', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        return context


class PhilosophyListView(ListView):
    model = Post
    template_name = 'joseon/philosophy_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='철학').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(PhilosophyListView, self).get_context_data(**kwargs)

        context['progressivism_tops'] = Post.objects.filter(
                category__name='철학', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['centrism_tops'] = Post.objects.filter(
                Q(category__name='철학') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['conservatism_tops'] = Post.objects.filter(
                category__name='철학', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['progressivism_tops_mobile'] = Post.objects.filter(
                category__name='철학', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['centrism_tops_mobile'] = Post.objects.filter(
                Q(category__name='철학') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['conservatism_tops_mobile'] = Post.objects.filter(
                category__name='철학', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        return context


class LoveListView(ListView):
    model = Post
    template_name = 'joseon/love_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='연애').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(LoveListView, self).get_context_data(**kwargs)

        context['progressivism_tops'] = Post.objects.filter(
                category__name='연애', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['centrism_tops'] = Post.objects.filter(
                Q(category__name='연애') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['conservatism_tops'] = Post.objects.filter(
                category__name='연애', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['progressivism_tops_mobile'] = Post.objects.filter(
                category__name='연애', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['centrism_tops_mobile'] = Post.objects.filter(
                Q(category__name='연애') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['conservatism_tops_mobile'] = Post.objects.filter(
                category__name='연애', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        return context


class BAIListView(ListView):
    model = Post
    template_name = 'joseon/BAI_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='사간의글').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(BAIListView, self).get_context_data(**kwargs)

        context['progressivism_tops'] = Post.objects.filter(
                category__name='사간의글', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['centrism_tops'] = Post.objects.filter(
                Q(category__name='사간의글') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['conservatism_tops'] = Post.objects.filter(
                category__name='사간의글', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

        context['progressivism_tops_mobile'] = Post.objects.filter(
                category__name='사간의글', political_orientation='progressivism',
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['centrism_tops_mobile'] = Post.objects.filter(
                Q(category__name='사간의글') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        context['conservatism_tops_mobile'] = Post.objects.filter(
                category__name='사간의글', political_orientation='conservatism'
            ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[3:10]

        return context


class SecretListView(ListView):
    model = Post
    template_name = 'joseon/secret_list.html'
    context_object_name = 'posts'
    paginate_by = 30

    def get_queryset(self):
        return Post.objects.filter(category__name='비밀').annotate(comment_count=Count('comments'))


@login_required(login_url='login')
def joseon_detail(request, pk):
    post = Post.objects.select_related('author').prefetch_related('spear','shield','scrap').get(pk=pk)

    comments = Comment.objects.select_related('author').prefetch_related(
            'replies__author', 'up', 'down', 'replies__up', 'replies__down').filter(post=post, reply=None)

    comment_all = Comment.objects.filter(post=post)

    comment_top = Comment.objects.select_related('author').prefetch_related(
            'up', 'down').filter(post=post).order_by('-total','-created_date')[:3]

    jprofile = JProfile.objects.values('department', 'position', 'levels').get(user=request.user)

    if request.method =='POST':
        contents = request.POST.get('contents')
        reply_id = request.POST.get('comment_id')
        comment_qs = None
        if reply_id:
            comment_qs = Comment.objects.get(id=reply_id)
        comment = Comment.objects.create(post=post, author=request.user, contents=contents, reply=comment_qs)

        if post.nickname_check.filter(id=request.user.id).exists():
            first = Comment.objects.filter(post=post, author=request.user).first()
            comment.anonymous = first.anonymous
        else:
            post.nickname_check.add(request.user)
            post.save()
            name = make_nickname()
            comment.anonymous = name
        comment.save()

    context = {
        'post': post,
        'comments': comments,
        'comment_all' : comment_all,
        'comment_top' : comment_top,
        'get_total_scrap' : post.get_total_scrap(),
        'get_total_spear' : post.get_total_spear(),
        'get_total_shield' : post.get_total_shield(),
        'jprofile' : jprofile,
    }

    if request.is_ajax():
        html = render_to_string('joseon/section/comments.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'joseon/joseon_detail.html', context)


@login_required(login_url='login')
def politics(request):
    return render(request, 'joseon/politics_post.html')


@login_required(login_url='login')
def economy(request):
    return render(request, 'joseon/economy_post.html')


@login_required(login_url='login')
def society(request):
    return render(request, 'joseon/society_post.html')


@login_required(login_url='login')
def world(request):
    return render(request, 'joseon/world_post.html')


@login_required(login_url='login')
def ideology(request):
    return render(request, 'joseon/ideology_post.html')


@login_required(login_url='login')
def philosophy(request):
    return render(request, 'joseon/philosophy_post.html')


@login_required(login_url='login')
def love(request):
    return render(request, 'joseon/love_post.html')


@login_required(login_url='login')
def BAI(request):
    jprofile = JProfile.objects.only('department').get(user=request.user)
    item = Item.objects.only('refutation').get(user=request.user)

    if jprofile.department == 'BAI' and item.refutation >= 1:
        return render(request, 'joseon/BAI_post.html')
    elif jprofile.department != 'BAI':
        messages.info(request, "사간원만 작성할 수 있습니다. ")
        return HttpResponseRedirect(reverse('joseon:BAI_list'))
    elif item.refutation < 1:
        messages.info(request, "논박아이템이 없습니다. ")
        return HttpResponseRedirect(reverse('joseon:BAI_list'))


@login_required(login_url='login')
def secret(request):
    return render(request, 'joseon/secret_post.html')


def post_politics(request):
    title = request.POST['title']
    category = Category.objects.get(name='정치')
    contents = request.POST['contents']
    name = make_nickname()
    jprofile = JProfile.objects.only('political_orientation').get(user=request.user)
    qs = Post(
            title=title,
            category=category,
            contents=contents,
            author=request.user,
            anonymous=name,
            political_orientation=jprofile.political_orientation
        )
    qs.save()
    coin = Coin.objects.only('blackcoin').get(user=request.user)
    coin.blackcoin += 2
    coin.save()

    return HttpResponseRedirect(reverse('joseon:politics_list'))


def post_economy(request):
    title = request.POST['title']
    category = Category.objects.get(name='경제')
    contents = request.POST['contents']
    name = make_nickname()
    jprofile = JProfile.objects.only('political_orientation').get(user=request.user)
    qs = Post(
            title=title,
            category=category,
            contents=contents,
            author=request.user,
            anonymous=name,
            political_orientation=jprofile.political_orientation
        )
    qs.save()
    coin = Coin.objects.only('blackcoin').get(user=request.user)
    coin.blackcoin += 2
    coin.save()

    return HttpResponseRedirect(reverse('joseon:economy_list'))


def post_society(request):
    title = request.POST['title']
    category = Category.objects.get(name='사회')
    contents = request.POST['contents']
    name = make_nickname()
    jprofile = JProfile.objects.only('political_orientation').get(user=request.user)
    qs = Post(
            title=title,
            category=category,
            contents=contents,
            author=request.user,
            anonymous=name,
            political_orientation=jprofile.political_orientation
        )
    qs.save()
    coin = Coin.objects.only('blackcoin').get(user=request.user)
    coin.blackcoin += 2
    coin.save()

    return HttpResponseRedirect(reverse('joseon:society_list'))


def post_world(request):
    title = request.POST['title']
    category = Category.objects.get(name='세계')
    contents = request.POST['contents']
    name = make_nickname()
    jprofile = JProfile.objects.only('political_orientation').get(user=request.user)
    qs = Post(
            title=title,
            category=category,
            contents=contents,
            author=request.user,
            anonymous=name,
            political_orientation=jprofile.political_orientation
        )
    qs.save()
    coin = Coin.objects.only('blackcoin').get(user=request.user)
    coin.blackcoin += 2
    coin.save()

    return HttpResponseRedirect(reverse('joseon:world_list'))


def post_ideology(request):
    title = request.POST['title']
    category = Category.objects.get(name='이념')
    contents = request.POST['contents']
    name = make_nickname()
    jprofile = JProfile.objects.only('political_orientation').get(user=request.user)
    qs = Post(
            title=title,
            category=category,
            contents=contents,
            author=request.user,
            anonymous=name,
            political_orientation=jprofile.political_orientation
        )
    qs.save()
    coin = Coin.objects.only('blackcoin').get(user=request.user)
    coin.blackcoin += 2
    coin.save()

    return HttpResponseRedirect(reverse('joseon:ideology_list'))


def post_philosophy(request):
    title = request.POST['title']
    category = Category.objects.get(name='철학')
    contents = request.POST['contents']
    name = make_nickname()
    jprofile = JProfile.objects.only('political_orientation').get(user=request.user)
    qs = Post(
            title=title,
            category=category,
            contents=contents,
            author=request.user,
            anonymous=name,
            political_orientation=jprofile.political_orientation
        )
    qs.save()
    coin = Coin.objects.only('blackcoin').get(user=request.user)
    coin.blackcoin += 2
    coin.save()

    return HttpResponseRedirect(reverse('joseon:philosophy_list'))


def post_love(request):
    title = request.POST['title']
    category = Category.objects.get(name='연애')
    contents = request.POST['contents']
    name = make_nickname()
    jprofile = JProfile.objects.only('political_orientation').get(user=request.user)
    qs = Post(
            title=title,
            category=category,
            contents=contents,
            author=request.user,
            anonymous=name,
            political_orientation=jprofile.political_orientation
        )
    qs.save()
    coin = Coin.objects.only('blackcoin').get(user=request.user)
    coin.blackcoin += 2
    coin.save()

    return HttpResponseRedirect(reverse('joseon:love_list'))


def post_BAI(request):
    title = request.POST['title']
    category = Category.objects.get(name='사간의글')
    contents = request.POST['contents']
    name = make_nickname()
    jprofile = JProfile.objects.only('political_orientation').get(user=request.user)
    qs = Post(
            title=title,
            category=category,
            contents=contents,
            author=request.user,
            anonymous=name,
            political_orientation=jprofile.political_orientation
        )
    qs.save()
    coin = Coin.objects.only('blackcoin').get(user=request.user)
    coin.blackcoin += 2
    coin.save()
    item = Item.objects.only('refutation').get(user=request.user)
    item.refutation -= 1
    item.save()

    return HttpResponseRedirect(reverse('joseon:BAI_list'))


def post_secret(request):
    title = request.POST['title']
    category = Category.objects.get(name='비밀')
    contents = request.POST['contents']
    name = make_nickname()
    jprofile = JProfile.objects.only('political_orientation').get(user=request.user)
    qs = Post(
            title=title,
            category=category,
            contents=contents,
            author=request.user,
            anonymous=name,
            political_orientation=jprofile.political_orientation
        )
    qs.save()

    return HttpResponseRedirect(reverse('joseon:secret_list'))


def add_spear(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    item = Item.objects.get(user=request.user)
    if post.author != request.user:
        if post.spear.filter(id=request.user.id).exists():
            messages.info(request, "창을 이미 사용하였습니다.")
        else:
            if item.spear >= 1:
                post.spear.add(request.user)
                post.all_recommend += 1
                post.save()
                item.spear -= 1
                item.save()
            else:
                messages.info(request, "창이 없습니다.")
    else:
        messages.info(request, "불가능합니다.")

    context = {
        'post' : post,
        'get_total_spear' : post.get_total_spear()
    }
    if request.is_ajax():
        html = render_to_string('joseon/section/spear_section.html', context, request=request)
    return JsonResponse({'form': html})


def add_shield(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    item = Item.objects.get(user=request.user)
    if post.author != request.user:
        if post.shield.filter(id=request.user.id).exists():
            messages.info(request, "방패를 이미 사용하였습니다.")
        else:
            if item.shield >= 1:
                post.shield.add(request.user)
                post.all_recommend -= 1
                post.save()
                item.shield -= 1
                item.save()
            else:
                messages.info(request, "방패가 없습니다.")
    else:
        messages.info(request, "불가능합니다.")

    context = {
        'post' : post,
        'get_total_shield' : post.get_total_shield()
    }
    if request.is_ajax():
        html = render_to_string('joseon/section/shield_section.html' , context, request=request)
    return JsonResponse({'form': html})


def lower_credibility(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    if post.author != request.user:
        if post.credibility.filter(id=request.user.id).exists():
            messages.info(request, "이미 신빙성을 낮추었습니다.")
        else:
            post.credibility.add(request.user)
            post.total_credibility -= 1
            post.save()
    else:
        messages.info(request, "불가능합니다.")

    context = {
        'post' : post,
    }
    if request.is_ajax():
        html = render_to_string('joseon/section/credibility_section.html' , context, request=request)
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
        html = render_to_string('joseon/section/scrap_section.html' , context, request=request)
    return JsonResponse({'form': html})


def user_scrap(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.scrap.filter(id=request.user.id).exists():
        post.scrap.remove(request.user)

    return redirect(request.META['HTTP_REFERER'])


def add_spearOfGod(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    item = Item.objects.get(user=request.user)
    if post.author != request.user:
        if post.spearOfGod.filter(id=request.user.id).exists():
            messages.info(request, "모든 것을 뚫는 창을 이미 사용하였습니다.")
        else:
            if item.spearOfGod >= 1:
                post.spearOfGod.add(request.user)
                post.all_recommend += 10000
                post.save()
                item.spearOfGod -= 1
                item.save()
            else:
                messages.info(request, "모든 것을 뚫는 창이 없습니다.")
    else:
        messages.info(request, "불가능합니다.")

    context = {
        'post' : post,
    }
    if request.is_ajax():
        html = render_to_string('joseon/section/spearOfGod_section.html', context, request=request)
    return JsonResponse({'form': html})


def add_shieldOfGod(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    item = Item.objects.get(user=request.user)
    if post.author != request.user:
        if post.shieldOfGod.filter(id=request.user.id).exists():
            messages.info(request, "모든 것을 막는 방패를 이미 사용하였습니다.")
        else:
            if item.shieldOfGod >= 1:
                post.shieldOfGod.add(request.user)
                post.all_recommend -= 10000
                post.save()
                item.shieldOfGod -= 1
                item.save()
            else:
                messages.info(request, "모든 것을 막는 방패가 없습니다.")
    else:
        messages.info(request, "불가능합니다.")

    context = {
        'post' : post,
    }
    if request.is_ajax():
        html = render_to_string('joseon/section/shieldOfGod_section.html', context, request=request)
    return JsonResponse({'form': html})


def get_sword(request):
    kind = request.POST.get('kind')
    if request.method == 'POST':
        giver_item = Item.objects.get(user=request.user)
        if giver_item.sword >= 1:
            giver_item.sword -= 1
            giver_item.save()
            recipient = User.objects.get(id=request.POST.get('rec_author'))
            recipient_item = Item.objects.get(user=recipient)
            recipient_item.getsword += 1
            recipient_item.save()
            messages.info(request, "검을 성공적으로 사용하였습니다.")
            if recipient_item.get_total_sword() >= 10:
                group = Group.objects.get(name='Joseon_Accused')
                recipient.groups.add(group)
                recipient_item.getsword = 0
                recipient_item.armor = 0
                recipient_item.save()
                if kind == 'post':
                    post = get_object_or_404(Post, id=request.POST.get('id'))
                    post.contents = '작성자가 받은 검이 누적되어 해당 글은 제재되었습니다.'
                    post.title = '작성자가 받은 검이 누적되어 해당 글은 제재되었습니다.'
                    post.save()
                else:
                    comment = get_object_or_404(Comment, id=request.POST.get('id'))
                    comment.delete()
        else:
            messages.info(request, "검이 없습니다.")

    if request.is_ajax():
        if kind == 'post':
            html = render_to_string('joseon/section/sword_section.html', request=request)
        elif kind == 'comment':
            html = render_to_string('joseon/section/comment_sword_section.html', request=request)
        elif kind == 'reply':
            html = render_to_string('joseon/section/reply_sword_section.html', request=request)
        elif kind == 'top':
            html = render_to_string('joseon/section/top_sword_section.html', request=request)
    return JsonResponse({'form': html})


def recommended(request):
    kind = request.POST.get('kind')
    if request.method =='POST':
        giver_item = Item.objects.get(user=request.user)
        if giver_item.reference_letter >= 1:
            giver_item.reference_letter -= 1
            giver_item.save()
            recipient = User.objects.get(id=request.POST.get('rec_author'))
            recipient_item = Item.objects.get(user=recipient)
            recipient_coin = Coin.objects.get(user=recipient)
            recipient_item.recommended += 1
            recipient_item.save()
            recipient_coin.bluecoin += 5
            recipient_coin.greencoin += 5
            recipient_coin.orangecoin += 5
            recipient_coin.pinkcoin += 5
            recipient_coin.purplecoin += 5
            recipient_coin.save()
            messages.info(request, "인사추천을 성공적으로 하였습니다.")
        else:
            messages.info(request, "인사추천권이 없습니다.")

    if request.is_ajax():
        if kind == 'post':
            html = render_to_string('joseon/section/recommended_section.html', request=request)
        elif kind == 'comment':
            html = render_to_string('joseon/section/comment_recommended_section.html', request=request)
        elif kind == 'reply':
            html = render_to_string('joseon/section/reply_recommended_section.html', request=request)
        elif kind == 'top':
            html = render_to_string('joseon/section/top_recommended_section.html', request=request)
    return JsonResponse({'form': html})


def impeached(request):
    kind = request.POST.get('kind')
    if request.method =='POST':
        giver_item = Item.objects.get(user=request.user)
        if giver_item.impeachment >= 1:
            giver_item.impeachment -= 1
            giver_item.save()
            recipient = User.objects.get(id=request.POST.get('rec_author'))
            recipient_item = Item.objects.get(user=recipient)
            recipient_item.impeached += 1
            recipient_item.save()
            recipient_jprofile = JProfile.objects.get(user=recipient)
            if recipient_item.get_total_impeached() == 30:
                recipient_jprofile.levels = 13
                recipient_jprofile.department = 'd'
                recipient_jprofile.position = None
                recipient_jprofile.save()
                recipient_item.impeached = 0
                recipient_item.impeachment_shield = 0
                recipient_item.save()
                if recipient.groups.filter(name='Ranker').exists():
                    group = Group.objects.get(name='Ranker')
                    recipient.groups.remove(group)
            messages.info(request, "탄핵권을 성공적으로 행사하였습니다.")
        else:
            messages.info(request, "탄핵권이 없습니다.")

    if request.is_ajax():
        if kind == 'post':
            html = render_to_string('joseon/section/impeached_section.html', request=request)
        elif kind == 'comment':
            html = render_to_string('joseon/section/comment_impeached_section.html', request=request)
        elif kind == 'reply':
            html = render_to_string('joseon/section/reply_impeached_section.html', request=request)
        elif kind == 'top':
            html = render_to_string('joseon/section/top_impeached_section.html', request=request)
    return JsonResponse({'form': html})


def get_swordOfGod(request):
    kind = request.POST.get('kind')
    if request.method =='POST':
        giver_item = Item.objects.get(user=request.user)
        if giver_item.swordOfGod >= 1:
            giver_item.swordOfGod -= 1
            giver_item.save()
            recipient = User.objects.get(id=request.POST.get('rec_author'))
            recipient_item = Item.objects.get(user=recipient)
            recipient_item.getsword += 100
            recipient_item.save()
            messages.info(request, "모든 것을 뚫는 검을 성공적으로 사용하였습니다.")
            if recipient_item.get_total_sword() >= 10:
                group = Group.objects.get(name='Joseon_Accused')
                recipient.groups.add(group)
                recipient_item.getsword = 0
                recipient_item.armor = 0
                recipient_item.save()
        else:
            messages.info(request, "모든것을 뚫는 검이 없습니다.")

    if request.is_ajax():
        if kind == 'post':
            html = render_to_string('joseon/section/swordOfGod_section.html', request=request)
        elif kind == 'comment':
            html = render_to_string('joseon/section/comment_swordOfGod_section.html', request=request)
        elif kind == 'reply':
            html = render_to_string('joseon/section/reply_swordOfGod_section.html', request=request)
        elif kind == 'top':
            html = render_to_string('joseon/section/top_swordOfGod_section.html', request=request)
    return JsonResponse({'form': html})


def up_comment(request):
    comment = get_object_or_404(Comment, id=request.POST.get('id'))
    kind = request.POST.get('kind')
    if comment.author != request.user:
        if comment.up.filter(id=request.user.id).exists():
            messages.info(request, "이미 UP하였습니다.")
        else:
            comment.up.add(request.user)
            comment.total += 1
            comment.save()
    else:
        messages.info(request, "불가능 합니다.")

    if kind == 'comment':
        context = {
            'comment' : comment,
        }

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
            html = render_to_string('joseon/section/comment_up_section.html', context, request=request)
        elif kind == 'reply':
            html = render_to_string('joseon/section/reply_up_section.html', context, request=request)
        elif kind == 'top':
            html = render_to_string('joseon/section/top_up_section.html', context, request=request)
    return JsonResponse({'form': html})


def down_comment(request):
    comment = get_object_or_404(Comment, id=request.POST.get('id'))
    kind = request.POST.get('kind')
    if comment.author != request.user:
        if comment.down.filter(id=request.user.id).exists():
            messages.info(request, "이미 Down하였습니다.")
        else:
            comment.down.add(request.user)
            comment.total -= 1
            comment.save()
    else:
        messages.info(request, "불가능합니다.")

    if kind == 'comment':
        context = {
            'comment' : comment,
        }

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
            html = render_to_string('joseon/section/comment_down_section.html', context, request=request)
        elif kind == 'reply':
            html = render_to_string('joseon/section/reply_down_section.html', context, request=request)
        elif kind == 'top':
            html = render_to_string('joseon/section/top_down_section.html', context, request=request)
    return JsonResponse({'form': html})


def make_nickname():
    adj = open('joseon/adjective.txt', mode='r', encoding='utf-8')
    adjline = adj.readlines()
    adj.close()
    adjective = random.choice(adjline)
    words = open('joseon/word.txt', mode='r', encoding='utf-8')
    wordsline = words.readlines()
    words.close()
    word = random.choice(wordsline)
    name = (adjective + " " + word)

    return name


# class UserPostListView(ListView):
#     model = Post
#     template_name = 'core/user_posts.html'
#     context_object_name = 'posts'
#     paginate_by = 15
#
#     def get_queryset(self):
#         return Post.objects.filter(author__id=self.kwargs.get('user_id')).only(
#             'title', 'contents', 'date_posted', 'anonymous').order_by('-date_posted')
#
#     def get_context_data(self, **kwargs):
#         context = super(UserPostListView, self).get_context_data(**kwargs)
#         context['ranker'] = Ranker.objects.filter(user__id=self.kwargs.get('user_id')).values('nickname')
#         return context
#
#
# def ratelimited_error(request, exception):
#     messages.info(request, '일정시간 후에 가능합니다')
#
#     return redirect(request.META['HTTP_REFERER'])
