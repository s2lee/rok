from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, JProfileUpdateForm, ProfileForm, JProfileForm
from .models import Profile, JProfile, Coin, Item, Certificate, UserKey, Ranker
from django.db.models.expressions import Window
from django.db.models.functions import Rank
from django.db.models import F
from django.contrib.auth.models import User
from joseon.models import Post
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        jprofile_form = JProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() and jprofile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            profile_form =  ProfileForm(request.POST, instance=user.profile)
            profile_form.full_clean()
            profile_form.save()
            jprofile_form = JProfileForm(request.POST, instance=user.jprofile)
            jprofile_form.full_clean()
            jprofile_form.save()
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
        jprofile_form = JProfileForm()

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
        'jprofile_form' : jprofile_form

    }
    return render(request, 'users/register.html', context)


def register_confirm(request):
    return render(request, 'users/register_confirm.html')

@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    item = Item.objects.get(user=request.user)
    ss_index = coin.purplecoin*7 + coin.pinkcoin*5 + coin.orangecoin*3 + item.recommended*25
    context = {
        'profile': profile,
        'jprofile' : jprofile,
        'ss_index' : ss_index
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def Updateprofile(request):
    if request.method == 'POST':
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_update_form.is_valid():
            profile_update_form.save()
            return redirect('profile')
    else:
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'profile_update_form': profile_update_form

    }
    return render(request, 'users/profile_update.html', context)


@login_required(login_url='login')
def jprofile(request):
    jprofile = JProfile.objects.select_related('user').get(user=request.user)
    item = Item.objects.select_related('user').get(user=request.user)
    ranker = Ranker.objects.select_related('user').get(user=request.user)
    profile = Profile.objects.select_related('user').get(user=request.user)
    ranking = Ranker.objects.select_related('user').annotate(
            rank=Window(
                expression=Rank(),
                order_by=F('rankpoint').desc()
            ),
        )

    context = {
        'jprofile': jprofile,
        'item' : item,
        'profile' : profile,
        'get_total_impeached' : item.get_total_impeached(),
        'ranker' : ranker,
        'ranking' : ranking
    }
    return render(request, 'users/jprofile.html', context)


@login_required(login_url='login')
def Updatejprofile(request):
    if request.method == 'POST':
        jprofile_update_form = JProfileUpdateForm(request.POST, request.FILES, instance=request.user.jprofile)
        if jprofile_update_form.is_valid():
            jprofile_update_form.save()
            return redirect('jprofile')

    else:
        jprofile_update_form = JProfileUpdateForm(instance=request.user.jprofile)

    context = {
        'jprofile_update_form': jprofile_update_form,
    }
    return render(request, 'users/jprofile_update.html', context)


@login_required(login_url='login')
def inventory(request):
    coin = Coin.objects.get(user=request.user)
    item = Item.objects.get(user=request.user)
    certificate = Certificate.objects.get(user=request.user)
    userkey = UserKey.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)

    context = {
        'coin': coin,
        'item': item,
        'certificate' : certificate,
        'userkey' : userkey,
        'jprofile' : jprofile,
        'get_total_sword' : item.get_total_sword(),
        'get_total_impeached' : item.get_total_impeached(),
    }

    return render(request, 'users/inventory.html', context)

@login_required(login_url='login')
def view_scrap(request):
    user = request.user
    crazylab_scraps = user.crazylab_scrap.select_related('author').prefetch_related('author__profile').all()
    joseon_scraps = user.joseon_scrap.select_related('author').all()
    reality_scraps = user.reality_scrap.select_related('author').prefetch_related('author__profile').all()
    context = {
        'crazylab_scraps' : crazylab_scraps,
        'joseon_scraps' : joseon_scraps,
        'reality_scraps' : reality_scraps
        }

    return render(request, "users/view_scrap.html", context)


def view_ranking(request):
    ranking = Ranker.objects.select_related('user').annotate(
            rank=Window(
                expression=Rank(),
                order_by=F('rankpoint').desc()
            ),
        )

    context = {
        'ranking' : ranking,
    }

    return render(request, "core/view_ranking.html", context)


def get_user_profile(request, nickname):
    profile = Profile.objects.get(nickname=nickname)


    context = {
        'profile' : profile,
    }

    return render(request, 'core/user_profile.html', context)


def HowToPlay(request):
    return render(request, 'users/HowToPlay.html')
