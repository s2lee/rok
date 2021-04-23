from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import Profile, JProfile, Coin, Item, Certificate, UserKey, Ranker, Classification
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from crazylab.models import Post as CrazylabPost, Category as CrazylabCategory
from joseon.models import Post as JoseonPost
from reality.models import Post as RealityPost, Category as RealityCategory
from django.db.models import Q, Count
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from django import db

def home(request):
    crazylab_publicidea =  CrazylabPost.objects.filter(category__name='공익아이디어').select_related('author').prefetch_related(
        'author__profile').annotate(comment_count=Count('comments')).order_by('-date_posted')[:47]

    tops = CrazylabPost.objects.filter(category__name='공익아이디어').annotate(
        comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:5]

    progressivism_tops = JoseonPost.objects.filter(
            category__name='정치', political_orientation='progressivism',
        ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

    centrism_tops = JoseonPost.objects.filter(
            Q(category__name='정치') & (Q(political_orientation='centrism') | Q(political_orientation='default'))
        ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

    conservatism_tops = JoseonPost.objects.filter(
            category__name='정치', political_orientation='conservatism'
        ).annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:3]

    reality_poetry = RealityPost.objects.filter(category__name='시').order_by('-all_recommend','-date_posted')[:3]

    context = {
        'crazylab_publicidea' : crazylab_publicidea,
        'progressivism_tops' : progressivism_tops,
        'centrism_tops' : centrism_tops,
        'conservatism_tops' : conservatism_tops,
        'reality_poetry' : reality_poetry,
        'tops' : tops
    }

    return render(request, 'home.html', context)


# 레벨업
def levelup(request):
    jprofile = JProfile.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)

    if jprofile.levels==18 and coin.blackcoin>=5:
        jprofile.levels-=1
        jprofile.save()
        coin.blackcoin-=5
        coin.save()

    elif jprofile.levels==17 and coin.blackcoin>=10:
        jprofile.levels-=1
        jprofile.save()
        coin.blackcoin-=10
        coin.save()

    elif jprofile.levels==16 and coin. blackcoin>=15:
        jprofile.levels-=1
        jprofile.save()
        coin.blackcoin-=15
        coin.save()

    elif jprofile.levels==15 and coin. blackcoin>=20:
        jprofile.levels-=1
        jprofile.save()
        coin.blackcoin-=20
        coin.save()

    elif jprofile.levels==14 and coin. blackcoin>=25:
        jprofile.levels-=1
        jprofile.save()
        coin.blackcoin-=25
        coin.save()

    elif jprofile.levels==13 and coin. blackcoin>=30:
        jprofile.levels-=1
        jprofile.save()
        coin.blackcoin-=30
        coin.save()

    elif jprofile.levels==12 and jprofile.department=='d':
        messages.error(request, "부서를 선택하세요")

    else:
        messages.error(request, "코인이 부족합니다")

    return redirect('jprofile')


def MSITlevelup(request):
    jprofile = JProfile.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    certificate = Certificate.objects.get(user=request.user)
    userkey = UserKey.objects.get(user=request.user)

    conditionSet = (
        jprofile.levels == 12
        and certificate.MSITcertificate >= 1
        and userkey.MSITfirstkey == 1
    )
    conditionSet2 = (
        jprofile.levels == 11
        and certificate.MSITcertificate >= 2
    )
    conditionSet3 = (
        jprofile.levels == 10
        and certificate.MSITcertificate >= 3
        and userkey.MSITsecondkey == 1
    )
    conditionSet4 = (
        jprofile.levels == 9
        and certificate.MSITcertificate >= 4
    )
    conditionSet5 = (
        jprofile.levels == 8
        and certificate.MSITcertificate >= 5
    )
    conditionSet6 = (
        jprofile.levels == 7
        and certificate.MSITcertificate >= 6
    )
    conditionSet7 = (
        jprofile.levels == 6
        and certificate.MSITcertificate >= 7
        and userkey.MSITthirdkey == 1
    )
    conditionSet8 = (
        jprofile.levels == 5
        and certificate.MSITcertificate >= 8
        and userkey.MSITfourthkey == 1
    )
    conditionSet9 = (
        jprofile.levels == 4
        and certificate.MSITcertificate >= 9
        and userkey.MSITfifthkey == 1
    )
    conditionSet10 = (
        jprofile.levels == 3
        and certificate.OPCcertificate >= 1
        and userkey.OPCfirstkey == 1
    )

    if conditionSet:
        jprofile.position = '공조좌랑'
        jprofile.levels -= 1
        jprofile.save()
        certificate.MSITcertificate -= 1
        certificate.save()

    elif conditionSet2:
        jprofile.levels -= 1
        jprofile.save()
        certificate.MSITcertificate -= 2
        certificate.save()

    elif conditionSet3:
        jprofile.position = '공조정랑'
        jprofile.levels -= 1
        jprofile.save()
        certificate.MSITcertificate -= 3
        certificate.save()

    elif conditionSet4:
        jprofile.levels -= 1
        jprofile.save()
        certificate.MSITcertificate -= 4
        certificate.save()

    elif conditionSet5:
        jprofile.levels -= 1
        jprofile.save()
        certificate.MSITcertificate -= 5
        certificate.save()

    elif conditionSet6:
        jprofile.levels -= 1
        jprofile.save()
        certificate.MSITcertificate -= 6
        certificate.save()

    elif conditionSet7:
        jprofile.levels -= 1
        jprofile.position = '공조참의'
        jprofile.save()
        certificate.MSITcertificate -= 7
        certificate.save()

    elif conditionSet8:
        jprofile.levels -= 1
        jprofile.position = '공조참판'
        jprofile.save()
        certificate.MSITcertificate -= 8
        certificate.save()

    elif conditionSet9:
        jprofile.levels -= 1
        jprofile.position = '공조판서'
        jprofile.save()
        certificate.MSITcertificate -= 9
        certificate.save()

    elif conditionSet10:
        jprofile.department = '의정부'
        jprofile.position = '우참찬'
        jprofile.save()
        certificate.OPCcertificate -= 1
        certificate.save()

    else:
        if jprofile.levels == 12 and certificate.MSITcertificate < 1:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 12 and userkey.MSITfirstkey == 0:
            messages.error(request, "Alpha1키가 필요합니다")

        elif jprofile.levels == 11 and certificate.MSITcertificate < 2:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 10 and certificate.MSITcertificate < 3:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 10 and userkey.MSITsecondkey == 0:
            messages.error(request, "Alpha2키가 필요합니다")

        elif jprofile.levels == 9 and certificate.MSITcertificate < 4:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 8 and certificate.MSITcertificate < 5:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 7 and certificate.MSITcertificate < 6:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 6 and certificate.MSITcertificate < 7:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 6 and userkey.MSITthirdkey == 0:
            messages.error(request, "Alpha3키가 필요합니다")

        elif jprofile.levels == 5 and certificate.MSITcertificate < 8:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 5 and userkey.MSITfourthkey == 0:
            messages.error(request, "Alpha4키가 필요합니다")

        elif jprofile.levels == 4 and certificate.MSITcertificate < 9:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 4 and userkey.MSITfifthkey == 0:
            messages.error(request, "Alpha5키가 필요합니다")

        elif jprofile.levels == 3 and certificate.OPCcertificate < 1:
            messages.error(request, "의정부 증서가 부족합니다")

        elif jprofile.levels == 3 and userkey.OPCfirstkey == 0:
            messages.error(request, "Omega1키가 필요합니다")

    return redirect('jprofile')


def MPMlevelup(request):
    jprofile = JProfile.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    certificate = Certificate.objects.get(user=request.user)
    userkey = UserKey.objects.get(user=request.user)

    conditionSet = (
        jprofile.levels == 12
        and certificate.MPMcertificate >= 1
        and userkey.MPMfirstkey == 1
    )
    conditionSet2 = (
        jprofile.levels == 11
        and certificate.MPMcertificate >= 2
    )
    conditionSet3 = (
        jprofile.levels == 10
        and certificate.MPMcertificate >= 3
        and userkey.MPMsecondkey == 1
    )
    conditionSet4 = (
        jprofile.levels == 9
        and certificate.MPMcertificate >= 4
    )
    conditionSet5 = (
        jprofile.levels == 8
        and certificate.MPMcertificate >= 5
    )
    conditionSet6 = (
        jprofile.levels == 7
        and certificate.MPMcertificate >= 6
    )
    conditionSet7 = (
        jprofile.levels == 6
        and certificate.MPMcertificate >= 7
        and userkey.MPMthirdkey == 1
    )
    conditionSet8 = (
        jprofile.levels == 5
        and certificate.MPMcertificate >= 8
        and userkey.MPMfourthkey == 1
    )
    conditionSet9 = (
        jprofile.levels == 4
        and certificate.MPMcertificate >= 9
        and userkey.MPMfifthkey == 1
    )
    conditionSet10 = (
        jprofile.levels == 3
        and certificate.OPCcertificate >= 1
        and userkey.OPCfirstkey == 1
    )

    if conditionSet:
        jprofile.position = '이조좌랑'
        jprofile.levels -= 1
        jprofile.save()
        certificate.MPMcertificate -= 1
        certificate.save()

    elif conditionSet2:
        jprofile.levels -= 1
        jprofile.save()
        certificate.MPMcertificate -= 2
        certificate.save()

    elif conditionSet3:
        jprofile.position = '이조정랑'
        jprofile.levels -= 1
        jprofile.save()
        certificate.MPMcertificate -= 3
        certificate.save()

    elif conditionSet4:
        jprofile.levels -= 1
        jprofile.save()
        certificate.MPMcertificate -= 4
        certificate.save()

    elif conditionSet5:
        jprofile.levels -= 1
        jprofile.save()
        certificate.MPMcertificate -= 5
        certificate.save()

    elif conditionSet6:
        jprofile.levels -= 1
        jprofile.save()
        certificate.MPMcertificate -= 6
        certificate.save()

    elif conditionSet7:
        jprofile.levels -= 1
        jprofile.position = '이조참의'
        jprofile.save()
        certificate.MPMcertificate -= 7
        certificate.save()

    elif conditionSet8:
        jprofile.levels -= 1
        jprofile.position = '이조참판'
        jprofile.save()
        certificate.MPMcertificate -= 8
        certificate.save()

    elif conditionSet9:
        jprofile.levels -= 1
        jprofile.position = '이조판서'
        jprofile.save()
        certificate.MPMcertificate -= 9
        certificate.save()

    elif conditionSet10:
        jprofile.department = '의정부'
        jprofile.position = '우참찬'
        jprofile.save()
        certificate.OPCcertificate -= 1
        certificate.save()

    else:
        if jprofile.levels == 12 and certificate.MPMcertificate < 1:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 12 and userkey.MPMfirstkey == 0:
            messages.error(request, "Delta1키가 필요합니다")

        elif jprofile.levels == 11 and certificate.MPMcertificate < 2:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 10 and certificate.MPMcertificate < 3:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 10 and userkey.MPMsecondkey == 0:
            messages.error(request, "Delta2키가 필요합니다")

        elif jprofile.levels == 9 and certificate.MPMcertificate < 4:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 8 and certificate.MPMcertificate < 5:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 7 and certificate.MPMcertificate < 6:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 6 and certificate.MPMcertificate < 7:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 6 and userkey.MPMthirdkey == 0:
            messages.error(request, "Delta3키가 필요합니다")

        elif jprofile.levels == 5 and certificate.MPMcertificate < 8:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 5 and userkey.MPMfourthkey == 0:
            messages.error(request, "Delta4키가 필요합니다")

        elif jprofile.levels == 4 and certificate.MPMcertificate < 9:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 4 and userkey.MPMfifthkey == 0:
            messages.error(request, "Delta5키가 필요합니다")

        elif jprofile.levels == 3 and certificate.OPCcertificate < 1:
            messages.error(request, "의정부 증서가 부족합니다")

        elif jprofile.levels == 3 and userkey.OPCfirstkey == 0:
            messages.error(request, "Omega1키가 필요합니다")

    return redirect('jprofile')


def BAIlevelup(request):
    jprofile = JProfile.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    certificate = Certificate.objects.get(user=request.user)
    userkey = UserKey.objects.get(user=request.user)

    conditionSet = (
        jprofile.levels == 12
        and certificate.BAIcertificate >= 1
        and userkey.BAIfirstkey == 1
    )
    conditionSet2 = (
        jprofile.levels == 11
        and certificate.BAIcertificate >= 2
    )
    conditionSet3 = (
        jprofile.levels == 10
        and certificate.BAIcertificate >= 3
        and userkey.BAIsecondkey == 1
    )
    conditionSet4 = (
        jprofile.levels == 9
        and certificate.BAIcertificate >= 4
    )
    conditionSet5 = (
        jprofile.levels == 8
        and certificate.BAIcertificate >= 5
    )
    conditionSet6 = (
        jprofile.levels == 7
        and certificate.BAIcertificate >= 6
        and userkey.BAIthirdkey == 1
    )
    conditionSet7 = (
        jprofile.levels == 6
        and certificate.BAIcertificate >= 7
        and userkey.BAIfourthkey == 1
    )
    conditionSet8 = (
        jprofile.levels == 5
        and certificate.OPCcertificate >= 1
        and userkey.OPCfirstkey == 1
    )

    if conditionSet:
        jprofile.position = '정언'
        jprofile.levels -= 1
        jprofile.save()
        certificate.BAIcertificate -= 1
        certificate.save()

    elif conditionSet2:
        jprofile.levels -= 1
        jprofile.save()
        certificate.BAIcertificate -= 2
        certificate.save()

    elif conditionSet3:
        jprofile.position = '헌납'
        jprofile.levels -= 1
        jprofile.save()
        certificate.BAIcertificate -= 3
        certificate.save()

    elif conditionSet4:
        jprofile.levels -= 1
        jprofile.save()
        certificate.BAIcertificate -= 4
        certificate.save()

    elif conditionSet5:
        jprofile.levels -= 1
        jprofile.save()
        certificate.BAIcertificate -= 5
        certificate.save()

    elif conditionSet6:
        jprofile.position = '사간'
        jprofile.levels -= 1
        jprofile.save()
        certificate.BAIcertificate -= 6
        certificate.save()

    elif conditionSet7:
        jprofile.position = '대사간'
        jprofile.levels -= 1
        jprofile.save()
        certificate.BAIcertificate -= 7
        certificate.save()

    elif conditionSet8:
        jprofile.department = '의정부'
        jprofile.position = '우참찬'
        jprofile.levels -= 2
        jprofile.save()
        certificate.OPCcertificate -= 1
        certificate.save()

    else:
        if jprofile.levels == 12 and certificate.BAIcertificate < 1:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 12 and userkey.BAIfirstkey == 0:
            messages.error(request, "Epsilon1키가 필요합니다")

        elif jprofile.levels == 11 and certificate.BAIcertificate < 2:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 10 and certificate.BAIcertificate < 3:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 10 and userkey.BAIsecondkey == 0:
            messages.error(request, "Epsilon2키가 필요합니다")

        elif jprofile.levels == 9 and certificate.BAIcertificate < 4:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 8 and certificate.BAIcertificate < 5:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 7 and certificate.BAIcertificate < 6:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 7 and userkey.BAIthirdkey == 0:
            messages.error(request, "Epsilon3키가 필요합니다")

        elif jprofile.levels == 6 and certificate.BAIcertificate < 7:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 6 and userkey.BAIfourthkey == 0:
            messages.error(request, "Epsilon4키가 필요합니다")

        elif jprofile.levels == 5 and certificate.OPCcertificate < 1:
            messages.error(request, "의정부 증서가 부족합니다")

        elif jprofile.levels == 5 and userkey.OPCfirstkey == 0:
            messages.error(request, "Omega1키가 필요합니다")

    return redirect('jprofile')


def SPOlevelup(request):
    jprofile = JProfile.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    certificate = Certificate.objects.get(user=request.user)
    userkey = UserKey.objects.get(user=request.user)

    conditionSet = (
        jprofile.levels == 12
        and certificate.SPOcertificate >= 1
        and userkey.SPOfirstkey == 1
    )
    conditionSet2 = (
        jprofile.levels == 11
        and certificate.SPOcertificate >= 2
    )
    conditionSet3 = (
        jprofile.levels == 10
        and certificate.SPOcertificate >= 3
        and userkey.SPOsecondkey == 1
    )
    conditionSet4 = (
        jprofile.levels == 9
        and certificate.SPOcertificate >= 4
    )
    conditionSet5 = (
        jprofile.levels == 8
        and certificate.SPOcertificate >= 5
        and userkey.SPOthirdkey == 1
    )
    conditionSet6 = (
        jprofile.levels == 7
        and certificate.SPOcertificate >= 6
        and userkey.SPOfourthkey == 1
    )
    conditionSet7 = (
        jprofile.levels == 6
        and certificate.SPOcertificate >= 7
    )
    conditionSet8 = (
        jprofile.levels == 5
        and certificate.SPOcertificate >= 8
        and userkey.SPOfifthkey == 1
    )
    conditionSet9 = (
        jprofile.levels == 4
        and certificate.OPCcertificate >= 1
        and userkey.OPCfirstkey == 1
    )

    if conditionSet:
        jprofile.position = '감찰'
        jprofile.levels -= 1
        jprofile.save()
        certificate.SPOcertificate -= 1
        certificate.save()

    elif conditionSet2:
        jprofile.levels -= 1
        jprofile.save()
        certificate.SPOcertificate -= 2
        certificate.save()

    elif conditionSet3:
        jprofile.position = '지평'
        jprofile.levels -= 1
        jprofile.save()
        certificate.SPOcertificate -= 3
        certificate.save()

    elif conditionSet4:
        jprofile.levels -= 1
        jprofile.save()
        certificate.SPOcertificate -= 4
        certificate.save()

    elif conditionSet5:
        jprofile.position = '장령'
        jprofile.levels -= 1
        jprofile.save()
        certificate.SPOcertificate -= 5
        certificate.save()

    elif conditionSet6:
        jprofile.position = '집의'
        jprofile.levels -= 1
        jprofile.save()
        certificate.SPOcertificate -= 6
        certificate.save()

    elif conditionSet7:
        jprofile.levels -= 1
        jprofile.save()
        certificate.SPOcertificate -= 7
        certificate.save()

    elif conditionSet8:
        jprofile.levels -= 1
        jprofile.position = '대사헌'
        jprofile.save()
        certificate.SPOcertificate -= 8
        certificate.save()

    elif conditionSet9:
        jprofile.levels -= 1
        jprofile.department = '의정부'
        jprofile.position = '우참찬'
        jprofile.save()
        certificate.OPCcertificate -= 1
        certificate.save()

    else:
        if jprofile.levels == 12 and certificate.SPOcertificate < 1:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 12 and userkey.SPOfirstkey == 0:
            messages.error(request, "Beta1키가 필요합니다")

        elif jprofile.levels == 11 and certificate.SPOcertificate < 2:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 10 and certificate.SPOcertificate < 3:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 10 and userkey.SPOsecondkey == 0:
            messages.error(request, "Beta2키가 필요합니다")

        elif jprofile.levels == 9 and certificate.SPOcertificate < 4:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 8 and certificate.SPOcertificate < 5:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 8 and userkey.SPOthirdkey == 0:
            messages.error(request, "Beta3키가 필요합니다")

        elif jprofile.levels == 7 and certificate.SPOcertificate < 6:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 7 and userkey.SPOfourthkey == 0:
            messages.error(request, "Beta4키가 필요합니다")

        elif jprofile.levels == 6 and certificate.SPOcertificate < 7:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 5 and certificate.SPOcertificate < 8:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 5 and userkey.SPOfifthkey == 0:
            messages.error(request, "Beta5키가 필요합니다")

        elif jprofile.levels == 4 and certificate.OPCcertificate < 1:
            messages.error(request, "의정부 증서가 부족합니다")

        elif jprofile.levels == 4 and userkey.OPCfirstkey == 0:
            messages.error(request, "Omega1키가 필요합니다")

    return redirect('jprofile')


def NPAlevelup(request):
    jprofile = JProfile.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    certificate = Certificate.objects.get(user=request.user)
    userkey = UserKey.objects.get(user=request.user)

    conditionSet = (
        jprofile.levels == 12
        and certificate.NPAcertificate >= 1
    )
    conditionSet2 = (
        jprofile.levels == 11
        and certificate.NPAcertificate >= 2
        and userkey.NPAfirstkey == 1
    )
    conditionSet3 = (
        jprofile.levels == 10
        and certificate.NPAcertificate >= 3
    )
    conditionSet4 = (
        jprofile.levels == 9
        and certificate.NPAcertificate >= 4
        and userkey.NPAsecondkey == 1
    )
    conditionSet5 = (
        jprofile.levels == 8
        and certificate.NPAcertificate >= 5
    )
    conditionSet6 = (
        jprofile.levels == 7
        and certificate.NPAcertificate >= 6
    )
    conditionSet7 = (
        jprofile.levels == 6
        and certificate.NPAcertificate >= 7
    )
    conditionSet8 = (
        jprofile.levels == 5
        and certificate.NPAcertificate >= 8
        and userkey.NPAthirdkey == 1
    )
    conditionSet9 = (
        jprofile.levels == 4
        and certificate.NPAcertificate >= 9
        and userkey.NPAfourthkey == 1
    )
    conditionSet10 = (
        jprofile.levels == 3
        and certificate.NPAcertificate >= 10
        and userkey.NPAfifthkey == 1
    )
    conditionSet11 = (
        jprofile.levels == 2
        and certificate.OPCcertificate >= 3
        and userkey.OPCthirdkey == 1
    )

    if conditionSet:
        jprofile.levels -= 1
        jprofile.save()
        certificate.NPAcertificate -= 1
        certificate.save()

    elif conditionSet2:
        jprofile.position = '도사'
        jprofile.levels -= 1
        jprofile.save()
        certificate.NPAcertificate -= 2
        certificate.save()

    elif conditionSet3:
        jprofile.levels -= 1
        jprofile.save()
        certificate.NPAcertificate -= 3
        certificate.save()

    elif conditionSet4:
        jprofile.position = '경력'
        jprofile.levels -= 1
        jprofile.save()
        certificate.NPAcertificate -= 4
        certificate.save()

    elif conditionSet5:
        jprofile.levels -= 1
        jprofile.save()
        certificate.NPAcertificate -= 5
        certificate.save()

    elif conditionSet6:
        jprofile.levels -= 1
        jprofile.save()
        certificate.NPAcertificate -= 6
        certificate.save()

    elif conditionSet7:
        jprofile.levels -= 1
        jprofile.save()
        certificate.NPAcertificate -= 7
        certificate.save()

    elif conditionSet8:
        jprofile.position = '동지사'
        jprofile.levels -= 1
        jprofile.save()
        certificate.NPAcertificate -= 8
        certificate.save()

    elif conditionSet9:
        jprofile.position = '지사'
        jprofile.levels -= 1
        jprofile.save()
        certificate.NPAcertificate -= 9
        certificate.save()

    elif conditionSet10:
        jprofile.position = '판사'
        jprofile.levels -= 1
        jprofile.save()
        certificate.NPAcertificate -= 10
        certificate.save()

    elif conditionSet11:
        jprofile.department = '의정부'
        jprofile.position = '우찬성'
        jprofile.save()
        certificate.OPCcertificate -= 3
        certificate.save()

    else:
        if jprofile.levels == 12 and certificate.NPAcertificate < 1:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 11 and certificate.NPAcertificate < 2:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 11 and userkey.NPAfirstkey == 0:
            messages.error(request, "Gamma1키가 필요합니다")

        elif jprofile.levels == 10 and certificate.NPAcertificate < 3:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 9 and certificate.NPAcertificate < 4:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 9 and userkey.NPAsecondkey == 0:
            messages.error(request, "Gamma2키가 필요합니다")

        elif jprofile.levels == 8 and certificate.NPAcertificate < 5:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 7 and certificate.NPAcertificate < 6:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 6 and certificate.NPAcertificate < 7:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 5 and certificate.NPAcertificate < 8:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 5 and userkey.NPAthirdkey == 0:
            messages.error(request, "Gamma3키가 필요합니다")

        elif jprofile.levels == 4 and certificate.NPAcertificate < 9:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 4 and userkey.NPAfourthkey == 0:
            messages.error(request, "Gamma4키가 필요합니다")

        elif jprofile.levels == 3 and certificate.NPAcertificate < 10:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.levels == 3 and userkey.NPAfifthkey == 0:
            messages.error(request, "Gamma5키가 필요합니다")

        elif jprofile.levels == 2 and certificate.OPCcertificate < 3:
            messages.error(request, "의정부 증서가 부족합니다")

        elif jprofile.levels == 2 and userkey.OPCthirdkey == 0:
            messages.error(request, "Omega3키가 필요합니다")

    return redirect('jprofile')


def OPClevelup(request):
    jprofile = JProfile.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    certificate = Certificate.objects.get(user=request.user)
    userkey = UserKey.objects.get(user=request.user)

    conditionSet = (
        jprofile.position == '우참찬'
        and certificate.OPCcertificate >= 2
        and userkey.OPCfirstkey == 1
        and userkey.OPCsecondkey == 1
    )
    conditionSet2 = (
        jprofile.position == '좌참찬'
        and certificate.OPCcertificate >= 3
        and userkey.OPCsecondkey == 1
        and userkey.OPCthirdkey == 1
    )
    conditionSet3 = (
        jprofile.position == '우찬성'
        and certificate.OPCcertificate >= 4
        and userkey.OPCthirdkey == 1
        and userkey.OPCfourthkey == 1
    )
    conditionSet4 = (
        jprofile.position == '좌찬성'
        and certificate.OPCcertificate >= 5
        and userkey.OPCfourthkey == 1
        and userkey.OPCfifthkey == 1
    )
    conditionSet5 = (
        jprofile.position == '우의정'
        and certificate.OPCcertificate >= 6
        and userkey.OPCfifthkey == 1
        and userkey.OPCsixthkey == 1
    )
    conditionSet6 = (
        jprofile.position == '좌의정'
        and certificate.OPCcertificate >= 7
        and userkey.OPCsixthkey == 1
        and userkey.OPCseventhkey == 1
    )

    conditionSet7 = (
        jprofile.position == '영의정'
        and userkey.OPCseventhkey == 1
        and userkey.SSkey == 1
    )

    if conditionSet:
        jprofile.position = '좌참찬'
        jprofile.save()
        certificate.OPCcertificate -= 2
        certificate.save()

    elif conditionSet2:
        jprofile.position = '우찬성'
        jprofile.levels -= 1
        jprofile.save()
        certificate.OPCcertificate -= 3
        certificate.save()

    elif conditionSet3:
        jprofile.position = '좌찬성'
        jprofile.save()
        certificate.OPCcertificate -= 4
        certificate.save()

    elif conditionSet4:
        jprofile.position = '우의정'
        jprofile.levels -= 1
        jprofile.save()
        certificate.OPCcertificate -= 5
        certificate.save()

    elif conditionSet5:
        jprofile.position = '좌의정'
        jprofile.save()
        certificate.OPCcertificate -= 6
        certificate.save()

    elif conditionSet6:
        jprofile.position = '영의정'
        jprofile.save()
        certificate.OPCcertificate -= 7
        certificate.save()

    elif conditionSet7:
        jprofile.position = '랭커'
        jprofile.department = 'd'
        group = Group.objects.get(name='Ranker')
        request.user.groups.add(group)
        jprofile.save()

    else:
        if jprofile.position == '우참찬' and certificate.OPCcertificate < 2:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.position == '우참찬' and userkey.OPCsecondkey == 0:
            messages.error(request, "Omega2키가 필요합니다")

        elif jprofile.position == '좌참찬' and certificate.OPCcertificate < 3:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.position == '좌참찬' and userkey.OPCthirdkey == 0:
            messages.error(request, "Omega3키가 필요합니다")

        elif jprofile.position == '우찬성' and certificate.OPCcertificate < 4:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.position == '우찬성' and userkey.OPCfourthkey == 0:
            messages.error(request, "Omega4키가 필요합니다")

        elif jprofile.position == '좌찬성' and certificate.OPCcertificate < 5:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.position == '좌찬성' and userkey.OPCfifthkey == 0:
            messages.error(request, "Omega5키가 필요합니다")

        elif jprofile.position == '우의정' and certificate.OPCcertificate < 6:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.position == '우의정' and userkey.OPCsixthkey == 0:
            messages.error(request, "Omega6키가 필요합니다")

        elif jprofile.position == '좌의정'and certificate.OPCcertificate < 7:
            messages.error(request, "증서가 부족합니다")

        elif jprofile.position == '좌의정' and userkey.OPCseventhkey == 0:
            messages.error(request, "Omega7키가 필요합니다")

        elif jprofile.position == '영의정' and userkey.SSkey == 0:
            messages.error(request, "Ranker키가 필요합니다")

    return redirect('jprofile')


# 상점
@login_required(login_url='login')
def shop(request):
    jprofile = JProfile.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)

    context = {
        'coin' : coin,
        'jprofile' : jprofile,
    }

    return render(request, 'core/shop.html', context)


def buySpear(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        if coin.blackcoin >= count:
            item.spear += count
            item.save()
            coin.blackcoin -= count
            coin.save()
            messages.success(request, "창을 성공적으로 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")
        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyShield(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        if coin.blackcoin >= count:
            item.shield += count
            item.save()
            coin.blackcoin -= count
            coin.save()
            messages.success(request, "방패를 성공적으로 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")
        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buySword(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        jprofile = JProfile.objects.get(user=request.user)
        if jprofile.position == '도사':
            if coin.blackcoin >= count*18:
                item.sword += count
                item.save()
                coin.blackcoin -= count*18
                coin.save()
                messages.success(request, "칼을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '경력':
            if coin.blackcoin >= count*16:
                item.sword += count
                item.save()
                coin.blackcoin -= count*16
                coin.save()
                messages.success(request, "칼을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '동지사':
            if coin.blackcoin >= count*14:
                item.sword += count
                item.save()
                coin.blackcoin -= count*14
                coin.save()
                messages.success(request, "칼을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '지사':
            if coin.blackcoin >= count*12:
                item.sword += count
                item.save()
                coin.blackcoin -= count*12
                coin.save()
                messages.success(request, "칼을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '판사':
            if coin.blackcoin >= count*10:
                item.sword += count
                item.save()
                coin.blackcoin -= count*10
                coin.save()
                messages.success(request, "칼을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        else:
            if coin.blackcoin >= count*20:
                item.sword += count
                item.save()
                coin.blackcoin -= count*20
                coin.save()
                messages.success(request, "칼을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyArmor(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        if coin.blackcoin >= count*30:
            item.armor += count
            item.save()
            coin.blackcoin -= count*30
            coin.save()
            messages.success(request, "갑옷 성공적으로 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")
        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyLetter(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        if coin.blackcoin >= count*10:
            item.letter += count
            item.save()
            coin.blackcoin -= count*10
            coin.save()
            messages.success(request, "편지작성권을 성공적으로 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")
        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyStar(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        jprofile = JProfile.objects.get(user=request.user)
        if jprofile.position == '공조좌랑':
            if coin.blackcoin >= count*50:
                item.star += count
                item.save()
                coin.blackcoin -= count*50
                coin.save()
                messages.success(request, "별을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '공조정랑':
            if coin.blackcoin >= count*40:
                item.star += count
                item.save()
                coin.blackcoin -= count*40
                coin.save()
                messages.success(request, "별을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '공조참의':
            if coin.blackcoin >= count*30:
                item.star += count
                item.save()
                coin.blackcoin -= count*30
                coin.save()
                messages.success(request, "별을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '공조참판':
            if coin.blackcoin >= count*25:
                item.star += count
                item.save()
                coin.blackcoin -= count*25
                coin.save()
                messages.success(request, "별을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '공조판서':
            if coin.blackcoin >= count*20:
                item.star += count
                item.save()
                coin.blackcoin -= count*20
                coin.save()
                messages.success(request, "별을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyReference_Letter(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        jprofile = JProfile.objects.get(user=request.user)
        if jprofile.position == '이조좌랑':
            if coin.blackcoin >= count*80:
                item.reference_letter += count
                item.save()
                coin.blackcoin -= count*80
                coin.save()
                messages.success(request, "추천서를 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '이조정랑':
            if coin.blackcoin >= count*60:
                item.reference_letter += count
                item.save()
                coin.blackcoin -= count*60
                coin.save()
                messages.success(request, "추천서를 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '이조참의':
            if coin.blackcoin >= count*40:
                item.reference_letter += count
                item.save()
                coin.blackcoin -= count*40
                coin.save()
                messages.success(request, "추천서를 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '이조참판':
            if coin.blackcoin >= count*30:
                item.reference_letter += count
                item.save()
                coin.blackcoin -= count*30
                coin.save()
                messages.success(request, "추천서를 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '이조판서':
            if coin.blackcoin >= count*20:
                item.reference_letter += count
                item.save()
                coin.blackcoin -= count*20
                coin.save()
                messages.success(request, "추천서를 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyRefutation(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        jprofile = JProfile.objects.get(user=request.user)
        if jprofile.position == '정언':
            if coin.blackcoin >= count*50:
                item.refutation += count
                item.save()
                coin.blackcoin -= count*50
                coin.save()
                messages.success(request, "사간원아이템을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '헌납':
            if coin.blackcoin >= count*40:
                item.refutation += count
                item.save()
                coin.blackcoin -= count*40
                coin.save()
                messages.success(request, "사간원아이템을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '사간':
            if coin.blackcoin >= count*30:
                item.refutation += count
                item.save()
                coin.blackcoin -= count*30
                coin.save()
                messages.success(request, "사간원아이템을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '대사간':
            if coin.blackcoin >= count*20:
                item.refutation += count
                item.save()
                coin.blackcoin -= count*20
                coin.save()
                messages.success(request, "사간원아이템을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')

@login_required(login_url='login')
def buyImpeachment(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        jprofile = JProfile.objects.get(user=request.user)
        if jprofile.position == '감찰':
            if coin.blackcoin >= count*80:
                item.impeachment += count
                item.save()
                coin.blackcoin -= count*80
                coin.save()
                messages.success(request, "탄핵권을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '지평':
            if coin.blackcoin >= count*60:
                item.impeachment += count
                item.save()
                coin.blackcoin -= count*60
                coin.save()
                messages.success(request, "탄핵권을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '장령':
            if coin.blackcoin >= count*40:
                item.impeachment += count
                item.save()
                coin.blackcoin -= count*40
                coin.save()
                messages.success(request, "탄핵권을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '집의':
            if coin.blackcoin >= count*30:
                item.impeachment += count
                item.save()
                coin.blackcoin -= count*30
                coin.save()
                messages.success(request, "탄핵권을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '대사헌':
            if coin.blackcoin >= count*20:
                item.impeachment += count
                item.save()
                coin.blackcoin -= count*20
                coin.save()
                messages.success(request, "탄핵권을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buySpearOfGod(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        jprofile = JProfile.objects.get(user=request.user)
        if jprofile.position == '좌참찬':
            if coin.blackcoin >= count*300:
                item.spearOfGod += count
                item.save()
                coin.blackcoin -= count*300
                coin.save()
                messages.success(request, "모든 것을 뚫는 창을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '좌찬성':
            if coin.blackcoin >= count*250:
                item.spearOfGod += count
                item.save()
                coin.blackcoin -= count*250
                coin.save()
                messages.success(request, "모든 것을 뚫는 창을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.levels == 1:
            if coin.blackcoin >= count*200:
                item.spearOfGod += count
                item.save()
                coin.blackcoin -= count*200
                coin.save()
                messages.success(request, "모든 것을 뚫는 창을 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyShieldOfGod(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        jprofile = JProfile.objects.get(user=request.user)
        if jprofile.position == '우참찬':
            if coin.blackcoin >= count*300:
                item.shieldOfGod += count
                item.save()
                coin.blackcoin -= count*300
                coin.save()
                messages.success(request, "모든 것을 막는 방패를 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.position == '우찬성':
            if coin.blackcoin >= count*250:
                item.shieldOfGod += count
                item.save()
                coin.blackcoin -= count*250
                coin.save()
                messages.success(request, "모든 것을 막는 방패를 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        elif jprofile.levels == 1:
            if coin.blackcoin >= count*200:
                item.shieldOfGod += count
                item.save()
                coin.blackcoin -= count*200
                coin.save()
                messages.success(request, "모든 것을 막는 방패를 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')

def buySwordOfGod(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        jprofile = JProfile.objects.get(user=request.user)

        if coin.blackcoin >= count*100:
            item.swordOfGod += count
            item.save()
            coin.blackcoin -= count*100
            coin.save()
            messages.success(request, "모든 것을 자르는 칼을 성공적으로 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyImpeachment_Shield(request):
    try:
        count = int(request.POST['count'])
        item = Item.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        if request.user.groups.filter(name='Ranker').exists():
            if coin.blackcoin >= count*80:
                item.impeachment_shield += count
                item.save()
                coin.blackcoin -= count*80
                coin.save()
                messages.success(request, "탄핵 방패를 성공적으로 샀어요")
            else:
                messages.error(request, "코인이 부족합니다")

            return redirect('core:shop')
        else:
            messages.error(request, "랭커가 아닙니다.")
            return redirect('')

    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyRankPoint(request):
    try:
        count = int(request.POST['count'])
        coin = Coin.objects.get(user=request.user)
        ranker = Ranker.objects.get(user=request.user)
        conditionSet = (
            coin.bluecoin >= count*5
            and coin.greencoin >= count*5
            and coin.orangecoin >= count*5
            and coin.pinkcoin >= count*5
            and coin.purplecoin >= count*5
        )
        if request.user.groups.filter(name='Ranker').exists():
            if conditionSet:
                coin.bluecoin -= count*5
                coin.greencoin -= count*5
                coin.orangecoin -= count*5
                coin.pinkcoin -= count*5
                coin.purplecoin -= count*5
                coin.save()
                ranker.rankpoint += count
                ranker.save()
                messages.success(request, "랭크 포인트를 샀습니다.")
            else:
                messages.error(request, "코인이 부족합니다")

            return redirect('core:shop')
        else:
            messages.error(request, "랭커가 아닙니다.")
            return redirect('')

    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyMSIT(request):
    try:
        count = int(request.POST['count'])
        certificate = Certificate.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        conditionSet = (
            coin.bluecoin >= count
            and coin.greencoin >= count
            and coin.orangecoin >= count
            and coin.pinkcoin >= count
            and coin.purplecoin >= count*3
        )

        if conditionSet:
            certificate.MSITcertificate += count
            certificate.save()
            coin.bluecoin -= count
            coin.greencoin -= count
            coin.orangecoin -= count
            coin.pinkcoin -= count
            coin.purplecoin -= count*3
            coin.save()
            messages.success(request, "공조 증서를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")
        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyMPM(request):
    try:
        count = int(request.POST['count'])
        certificate = Certificate.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        conditionSet = (
            coin.bluecoin >= count
            and coin.greencoin >= count
            and coin.orangecoin >= count
            and coin.pinkcoin >= count*3
            and coin.purplecoin >= count
        )

        if conditionSet:
            certificate.MPMcertificate += count
            certificate.save()
            coin.bluecoin -= count
            coin.greencoin -= count
            coin.orangecoin -= count
            coin.pinkcoin -= count*3
            coin.purplecoin -= count
            coin.save()
            messages.success(request, "이조 증서를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")
        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyBAI(request):
    try:
        count = int(request.POST['count'])
        certificate = Certificate.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        conditionSet = (
            coin.bluecoin >= count
            and coin.greencoin >= count
            and coin.orangecoin >= count*2
            and coin.pinkcoin >= count*2
            and coin.purplecoin >= count
        )
        if conditionSet:
            certificate.BAIcertificate += count
            certificate.save()
            coin.bluecoin -= count
            coin.greencoin -= count
            coin.orangecoin -= count*2
            coin.pinkcoin -= count*2
            coin.purplecoin -= count
            coin.save()
            messages.success(request, "사간원 증서를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")
        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buySPO(request):
    try:
        count = int(request.POST['count'])
        certificate = Certificate.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        conditionSet = (
            coin.bluecoin >= count
            and coin.greencoin >= count
            and coin.orangecoin >= count*3
            and coin.pinkcoin >= count
            and coin.purplecoin >= count
        )
        if conditionSet:
            certificate.SPOcertificate += count
            certificate.save()
            coin.bluecoin -= count
            coin.greencoin -= count
            coin.orangecoin -= count*3
            coin.pinkcoin -= count
            coin.purplecoin -= count
            coin.save()
            messages.success(request, "사헌부 증서를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")
        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyNPA(request):
    try:
        count = int(request.POST['count'])
        certificate = Certificate.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        conditionSet = (
            coin.bluecoin >= count
            and coin.greencoin >= count
            and coin.orangecoin >= count
            and coin.pinkcoin >= count
            and coin.purplecoin >= count*2
        )
        if conditionSet:
            certificate.NPAcertificate += count
            certificate.save()
            coin.bluecoin -= count
            coin.greencoin -= count
            coin.orangecoin -= count*2
            coin.pinkcoin -= count
            coin.purplecoin -= count*2
            coin.save()
            messages.success(request, "의금부 증서를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")
        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyOPC(request):
    try:
        count = int(request.POST['count'])
        certificate = Certificate.objects.get(user=request.user)
        coin = Coin.objects.get(user=request.user)
        conditionSet = (
            coin.bluecoin >= count*3
            and coin.greencoin >= count*3
            and coin.orangecoin >= count*3
            and coin.pinkcoin >= count*3
            and coin.purplecoin >= count*3
        )
        if conditionSet:
            certificate.OPCcertificate += count
            certificate.save()
            coin.bluecoin -= count*3
            coin.greencoin -= count*3
            coin.orangecoin -= count*3
            coin.pinkcoin -= count*3
            coin.purplecoin -= count*3
            coin.save()
            messages.success(request, "의정부 증서를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")
        return redirect('core:shop')
    except ValueError:
        messages.error(request, "입력한 값이 없습니다.")
        return redirect('core:shop')


def buyMSITfirstkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MSITfirstkey == 0
        and jprofile.levels == 12
    )
    conditionSet2 = (
        coin.purplecoin >= 12
        and coin.pinkcoin >= 4
        and coin.orangecoin >= 4
    )

    if conditionSet:
        if conditionSet2:
            userkey.MSITfirstkey += 1
            userkey.save()
            coin.purplecoin -= 12
            coin.pinkcoin -= 4
            coin.orangecoin -= 4
            coin.save()
            messages.success(request, "Alpha1키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.MSITfirstkey == 1:
        messages.error(request, "이미 Alpha1키가 있습니다.")

    else:
        messages.error(request, "從六品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyMSITsecondkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MSITsecondkey == 0
        and userkey.MSITfirstkey == 1
        and jprofile.levels == 10
    )
    conditionSet2 = (
        coin.purplecoin >= 24
        and coin.pinkcoin >= 8
        and coin.orangecoin >= 8
    )

    if conditionSet:
        if conditionSet2:
            userkey.MSITsecondkey += 1
            userkey.save()
            coin.purplecoin -= 24
            coin.pinkcoin -= 8
            coin.orangecoin -= 8
            coin.save()
            messages.success(request, "Alpha2키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.MSITfirstkey == 0:
        messages.error(request, "Alpha1키가 없습니다")

    elif userkey.MSITsecondkey == 1:
        messages.error(request, "이미 Alpha2키가 있습니다.")

    else:
        messages.error(request, "從五品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyMSITthirdkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MSITthirdkey == 0
        and userkey.MSITsecondkey == 1
        and jprofile.levels == 6
    )
    conditionSet2 = (
        coin.purplecoin >= 48
        and coin.pinkcoin >= 16
        and coin.orangecoin >= 16
    )

    if conditionSet:
        if conditionSet2:
            userkey.MSITthirdkey += 1
            userkey.save()
            coin.purplecoin -= 48
            coin.pinkcoin -= 16
            coin.orangecoin -= 16
            coin.save()
            messages.success(request, "Alpha3키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.MSITsecondkey == 0:
        messages.error(request, "Alpha2키가 없습니다")

    elif userkey.MSITthirdkey == 1:
        messages.error(request, "이미 Alpha3키가 있습니다.")

    else:
        messages.error(request, "從三品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyMSITfourthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MSITfourthkey == 0
        and userkey.MSITthirdkey == 1
        and jprofile.levels == 5
    )
    conditionSet2 = (
        coin.purplecoin >= 96
        and coin.pinkcoin >= 32
        and coin.orangecoin >= 32
    )

    if conditionSet:
        if conditionSet2:
            userkey.MSITfourthkey += 1
            userkey.save()
            coin.purplecoin -= 96
            coin.pinkcoin -= 32
            coin.orangecoin -= 32
            coin.save()
            messages.success(request, "Alpha4키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.MSITthirdkey == 0:
        messages.error(request, "Alpha3키가 없습니다")

    elif userkey.MSITfourthkey == 1:
        messages.error(request, "이미 Alpha4키가 있습니다.")

    else:
        messages.error(request, "正三品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyMSITfifthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MSITfifthkey == 0
        and userkey.MSITfourthkey == 1
        and jprofile.levels == 4
    )
    conditionSet2 = (
        coin.purplecoin >= 192
        and coin.pinkcoin >= 64
        and coin.orangecoin >= 64
    )

    if conditionSet:
        if conditionSet2:
            userkey.MSITfifthkey += 1
            userkey.save()
            coin.purplecoin -= 192
            coin.pinkcoin -= 64
            coin.orangecoin -= 64
            coin.save()
            messages.success(request, "Alpha5키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.MSITfourthkey == 0:
        messages.error(request, "Alpha4키가 없습니다")

    elif userkey.MSITfifthkey == 1:
        messages.error(request, "이미 Alpha5키가 있습니다.")

    else:
        messages.error(request, "從二品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyMPMfirstkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MPMfirstkey == 0
        and jprofile.levels == 12
    )
    conditionSet2 = (
        coin.purplecoin >= 3
        and coin.pinkcoin >= 9
        and coin.orangecoin >= 3
    )

    if conditionSet:
        if conditionSet2:
            userkey.MPMfirstkey += 1
            userkey.save()
            coin.purplecoin -= 3
            coin.pinkcoin -= 9
            coin.orangecoin -= 3
            coin.save()
            messages.success(request, "Delta1키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.MPMfirstkey == 1:
        messages.error(request, "이미 Delta1키가 있습니다.")

    else:
        messages.error(request, "從六品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyMPMsecondkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MPMsecondkey == 0
        and userkey.MPMfirstkey == 1
        and jprofile.levels == 10
    )
    conditionSet2 = (
        coin.purplecoin >= 6
        and coin.pinkcoin >= 18
        and coin.orangecoin >= 6
    )

    if conditionSet:
        if conditionSet2:
            userkey.MPMsecondkey += 1
            userkey.save()
            coin.purplecoin -= 6
            coin.pinkcoin -= 18
            coin.orangecoin -= 6
            coin.save()
            messages.success(request, "Delta2키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.MPMfirstkey == 0:
        messages.error(request, "Delta1키가 없습니다")

    elif userkey.MPMsecondkey == 1:
        messages.error(request, "이미 Delta2키가 있습니다.")

    else:
        messages.error(request, "從五品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyMPMthirdkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MPMthirdkey == 0
        and userkey.MPMsecondkey == 1
        and jprofile.levels == 6
    )
    conditionSet2 = (
        coin.purplecoin >= 12
        and coin.pinkcoin >= 36
        and coin.orangecoin >= 12
    )

    if conditionSet:
        if conditionSet2:
            userkey.MPMthirdkey += 1
            userkey.save()
            coin.purplecoin -= 12
            coin.pinkcoin -= 36
            coin.orangecoin -= 12
            coin.save()
            messages.success(request, "Delta3키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.MPMsecondkey == 0:
        messages.error(request, "Delta2키가 없습니다")

    elif userkey.MPMthirdkey == 1:
        messages.error(request, "이미 Delta3키가 있습니다.")

    else:
        messages.error(request, "從三品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyMPMfourthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MPMfourthkey == 0
        and userkey.MPMthirdkey == 1
        and jprofile.levels == 5
    )
    conditionSet2 = (
        coin.purplecoin >= 24
        and coin.pinkcoin >= 72
        and coin.orangecoin >= 24
    )

    if conditionSet:
        if conditionSet2:
            userkey.MPMfourthkey += 1
            userkey.save()
            coin.purplecoin -= 24
            coin.pinkcoin -= 72
            coin.orangecoin -= 24
            coin.save()
            messages.success(request, "Delta4키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.MPMthirdkey == 0:
        messages.error(request, "Delta3키가 없습니다")

    elif userkey.MPMfourthkey == 1:
        messages.error(request, "이미 Delta4키가 있습니다.")

    else:
        messages.error(request, "正三品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyMPMfifthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MPMfifthkey == 0
        and userkey.MPMfourthkey == 1
        and jprofile.levels == 4
    )
    conditionSet2 = (
        coin.purplecoin >= 48
        and coin.pinkcoin >= 144
        and coin.orangecoin >= 48
    )

    if conditionSet:
        if conditionSet2:
            userkey.MPMfifthkey += 1
            userkey.save()
            coin.purplecoin -= 48
            coin.pinkcoin -= 144
            coin.orangecoin -= 48
            coin.save()
            messages.success(request, "Delta5키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.MPMfourthkey == 0:
        messages.error(request, "Delta4키가 없습니다")

    elif userkey.MPMfifthkey == 1:
        messages.error(request, "이미 Delta5키가 있습니다.")

    else:
        messages.error(request, "從二品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyBAIfirstkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.BAIfirstkey == 0
        and jprofile.levels == 12
    )
    conditionSet2 = (
        coin.purplecoin >= 5
        and coin.pinkcoin >= 10
        and coin.orangecoin >= 10
        and coin.greencoin >= 5
        and coin.bluecoin >= 5
    )

    if conditionSet:
        if conditionSet2:
            userkey.BAIfirstkey += 1
            userkey.save()
            coin.purplecoin -= 5
            coin.pinkcoin -= 10
            coin.orangecoin -= 10
            coin.greencoin -= 5
            coin.bluecoin -= 5
            coin.save()
            messages.success(request, "Epsilon1키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.BAIfirstkey == 1:
        messages.error(request, "이미 Epsilon1키가 있습니다.")

    else:
        messages.error(request, "從六品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyBAIsecondkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.BAIsecondkey == 0
        and userkey.BAIfirstkey == 1
        and jprofile.levels == 10
    )
    conditionSet2 = (
        coin.purplecoin >= 10
        and coin.pinkcoin >= 20
        and coin.orangecoin >= 20
        and coin.greencoin >= 10
        and coin.bluecoin >= 10
    )

    if conditionSet:
        if conditionSet2:
            userkey.BAIsecondkey += 1
            userkey.save()
            coin.purplecoin -= 10
            coin.pinkcoin -= 20
            coin.orangecoin -= 20
            coin.greencoin -= 10
            coin.bluecoin -= 10
            coin.save()
            messages.success(request, "Epsilon2키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.BAIfirstkey == 0:
        messages.error(request, "Epsilon1키가 없습니다")

    elif userkey.BAIsecondkey == 1:
        messages.error(request, "이미 Epsilon2키가 있습니다.")

    else:
        messages.error(request, "從五品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyBAIthirdkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.BAIthirdkey == 0
        and userkey.BAIsecondkey == 1
        and jprofile.levels == 7
    )
    conditionSet2 = (
        coin.purplecoin >= 20
        and coin.pinkcoin >= 40
        and coin.orangecoin >= 40
        and coin.greencoin >= 20
        and coin.bluecoin >= 20
    )

    if conditionSet:
        if conditionSet2:
            userkey.BAIthirdkey += 1
            userkey.save()
            coin.purplecoin -= 20
            coin.pinkcoin -= 40
            coin.orangecoin -= 40
            coin.greencoin -= 20
            coin.bluecoin -= 20
            coin.save()
            messages.success(request, "Epsilon3키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.BAIsecondkey == 0:
        messages.error(request, "Epsilon2키가 없습니다")

    elif userkey.BAIthirdkey == 1:
        messages.error(request, "이미 Epsilon3키가 있습니다.")

    else:
        messages.error(request, "正四品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyBAIfourthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.BAIfourthkey == 0
        and userkey.BAIthirdkey == 1
        and jprofile.levels == 6
    )
    conditionSet2 = (
        coin.purplecoin >= 40
        and coin.pinkcoin >= 80
        and coin.orangecoin >= 80
        and coin.greencoin >= 40
        and coin.bluecoin >= 40
    )

    if conditionSet:
        if conditionSet2:
            userkey.BAIfourthkey += 1
            userkey.save()
            coin.purplecoin -= 40
            coin.pinkcoin -= 80
            coin.orangecoin -= 80
            coin.greencoin -= 40
            coin.bluecoin -= 40
            coin.save()
            messages.success(request, "Epsilon4키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.BAIthirdkey == 0:
        messages.error(request, "Epsilon3키가 없습니다")

    elif userkey.BAIfourthkey == 1:
        messages.error(request, "이미 Epsilon4키가 있습니다.")

    else:
        messages.error(request, "從三品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buySPOfirstkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.SPOfirstkey == 0
        and jprofile.levels == 12
    )
    conditionSet2 = (
        coin.purplecoin >= 3
        and coin.pinkcoin >= 3
        and coin.orangecoin >= 9
    )

    if conditionSet:
        if conditionSet2:
            userkey.SPOfirstkey += 1
            userkey.save()
            coin.purplecoin -= 3
            coin.pinkcoin -= 3
            coin.orangecoin -= 9
            coin.save()
            messages.success(request, "Beta1키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.SPOfirstkey == 1:
        messages.error(request, "이미 Beta1키가 있습니다.")

    else:
        messages.error(request, "從六品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buySPOsecondkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.SPOsecondkey == 0
        and userkey.SPOfirstkey == 1
        and jprofile.levels == 10
    )
    conditionSet2 = (
        coin.purplecoin >= 6
        and coin.pinkcoin >= 6
        and coin.orangecoin >= 18
    )

    if conditionSet:
        if conditionSet2:
            userkey.SPOsecondkey += 1
            userkey.save()
            coin.purplecoin -= 6
            coin.pinkcoin -= 6
            coin.orangecoin -= 18
            coin.save()
            messages.success(request, "Beta2키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.SPOfirstkey == 0:
        messages.error(request, "Beta1키가 없습니다")

    elif userkey.SPOsecondkey == 1:
        messages.error(request, "이미 Beta2키가 있습니다.")

    else:
        messages.error(request, "從五品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buySPOthirdkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.SPOthirdkey == 0
        and userkey.SPOsecondkey == 1
        and jprofile.levels == 8
    )
    conditionSet2 = (
        coin.purplecoin >= 12
        and coin.pinkcoin >= 12
        and coin.orangecoin >= 36
    )

    if conditionSet:
        if conditionSet2:
            userkey.SPOthirdkey += 1
            userkey.save()
            coin.purplecoin -= 12
            coin.pinkcoin -= 12
            coin.orangecoin -= 36
            coin.save()
            messages.success(request, "Beta3키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.SPOsecondkey == 0:
        messages.error(request, "Beta2키가 없습니다")

    elif userkey.SPOthirdkey == 1:
        messages.error(request, "이미 Beta3키가 있습니다.")

    else:
        messages.error(request, "從四品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buySPOfourthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.SPOfourthkey == 0
        and userkey.SPOthirdkey == 1
        and jprofile.levels == 7
    )
    conditionSet2 = (
        coin.purplecoin >= 24
        and coin.pinkcoin >= 24
        and coin.orangecoin >= 72
    )

    if conditionSet:
        if conditionSet2:
            userkey.SPOfourthkey += 1
            userkey.save()
            coin.purplecoin -= 24
            coin.pinkcoin -= 24
            coin.orangecoin -= 72
            coin.save()
            messages.success(request, "Beta4키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.SPOthirdkey == 0:
        messages.error(request, "Beta3키가 없습니다")

    elif userkey.SPOfourthkey == 1:
        messages.error(request, "이미 Beta4키가 있습니다.")

    else:
        messages.error(request, "正四品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buySPOfifthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.SPOfifthkey == 0
        and userkey.SPOfourthkey == 1
        and jprofile.levels == 5
    )
    conditionSet2 = (
        coin.purplecoin >= 48
        and coin.pinkcoin >= 48
        and coin.orangecoin >= 144
    )

    if conditionSet:
        if conditionSet2:
            userkey.SPOfifthkey += 1
            userkey.save()
            coin.purplecoin -= 48
            coin.pinkcoin -= 48
            coin.orangecoin -= 144
            coin.save()
            messages.success(request, "Beta5키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.SPOfourthkey == 0:
        messages.error(request, "Beta4키가 없습니다")

    elif userkey.SPOfifthkey == 1:
        messages.error(request, "이미 Beta5키가 있습니다.")

    else:
        messages.error(request, "正三品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyNPAfirstkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.NPAfirstkey == 0
        and jprofile.levels == 11
    )
    conditionSet2 = (
        coin.purplecoin >= 4
        and coin.pinkcoin >= 2
        and coin.orangecoin >= 4
        and coin.greencoin >= 2
        and coin.bluecoin >= 2
    )

    if conditionSet:
        if conditionSet2:
            userkey.NPAfirstkey += 1
            userkey.save()
            coin.purplecoin -= 4
            coin.pinkcoin -= 2
            coin.orangecoin -= 4
            coin.greencoin -= 2
            coin.bluecoin -= 2
            coin.save()
            messages.success(request, "Gamma1키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.NPAfirstkey == 1:
        messages.error(request, "이미 Gamma1키가 있습니다.")

    else:
        messages.error(request, "正六品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyNPAsecondkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.NPAsecondkey == 0
        and userkey.NPAfirstkey == 1
        and jprofile.levels == 9
    )
    conditionSet2 = (
        coin.purplecoin >= 8
        and coin.pinkcoin >= 4
        and coin.orangecoin >= 8
        and coin.greencoin >= 4
        and coin.bluecoin >= 4
    )

    if conditionSet:
        if conditionSet2:
            userkey.NPAsecondkey += 1
            userkey.save()
            coin.purplecoin -= 8
            coin.pinkcoin -= 4
            coin.orangecoin -= 8
            coin.greencoin -= 4
            coin.bluecoin -= 4
            coin.save()
            messages.success(request, "Gamma2키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.NPAfirstkey == 0:
        messages.error(request, "Gamma1키가 없습니다")

    elif userkey.NPAsecondkey == 1:
        messages.error(request, "이미 Gamma2키가 있습니다.")

    else:
        messages.error(request, "正五品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyNPAthirdkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.NPAthirdkey == 0
        and userkey.NPAsecondkey == 1
        and jprofile.levels == 5
    )
    conditionSet2 = (
        coin.purplecoin >= 16
        and coin.pinkcoin >= 8
        and coin.orangecoin >= 16
        and coin.greencoin >= 8
        and coin.bluecoin >= 8
    )

    if conditionSet:
        if conditionSet2:
            userkey.NPAthirdkey += 1
            userkey.save()
            coin.purplecoin -= 16
            coin.pinkcoin -= 8
            coin.orangecoin -= 16
            coin.greencoin -= 8
            coin.bluecoin -= 8
            coin.save()
            messages.success(request, "Gamma3키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.NPAsecondkey == 0:
        messages.error(request, "Gamma2키가 없습니다")

    elif userkey.NPAthirdkey == 1:
        messages.error(request, "이미 Gamma3키가 있습니다.")

    else:
        messages.error(request, "正三品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyNPAfourthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.NPAfourthkey == 0
        and userkey.NPAthirdkey == 1
        and jprofile.levels == 4
    )
    conditionSet2 = (
        coin.purplecoin >= 32
        and coin.pinkcoin >= 16
        and coin.orangecoin >= 32
        and coin.greencoin >= 16
        and coin.bluecoin >= 16
    )

    if conditionSet:
        if conditionSet2:
            userkey.NPAfourthkey += 1
            userkey.save()
            coin.purplecoin -= 32
            coin.pinkcoin -= 16
            coin.orangecoin -= 32
            coin.greencoin -= 16
            coin.bluecoin -= 16
            coin.save()
            messages.success(request, "Gamma4키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.NPAthirdkey == 0:
        messages.error(request, "Gamma3키가 없습니다")

    elif userkey.NPAfourthkey == 1:
        messages.error(request, "이미 Gamma4키가 있습니다.")

    else:
        messages.error(request, "從二品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyNPAfifthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.NPAfifthkey == 0
        and userkey.NPAfourthkey == 1
        and jprofile.levels == 3
    )
    conditionSet2 = (
        coin.purplecoin >= 64
        and coin.pinkcoin >= 32
        and coin.orangecoin >= 64
        and coin.greencoin >= 32
        and coin.bluecoin >= 32
    )

    if conditionSet:
        if conditionSet2:
            userkey.NPAfifthkey += 1
            userkey.save()
            coin.purplecoin -= 64
            coin.pinkcoin -= 32
            coin.orangecoin -= 64
            coin.greencoin -= 32
            coin.bluecoin -=32
            coin.save()
            messages.success(request, "Gamma5키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.NPAfourthkey == 0:
        messages.error(request, "Gamma4키가 없습니다")

    elif userkey.NPAfifthkey == 1:
        messages.error(request, "이미 Gamma5키가 있습니다.")

    else:
        messages.error(request, "正二品이 되어야 살 수 있습니다.")

    return redirect('core:shop')


def buyOPCfirstkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.MSITfifthkey == 1
        or userkey.MPMfifthkey == 1
        or userkey.BAIfourthkey == 1
        or userkey.SPOfifthkey == 1
    )
    conditionSet2 = (
        coin.purplecoin >= 15
        and coin.pinkcoin >= 15
        and coin.orangecoin >= 15
        and coin.greencoin >= 15
        and coin.bluecoin >= 15
    )

    if conditionSet:
        if conditionSet2:
            userkey.OPCfirstkey += 1
            userkey.save()
            coin.purplecoin -= 15
            coin.pinkcoin -= 15
            coin.orangecoin -= 15
            coin.greencoin -= 15
            coin.bluecoin -= 15
            coin.save()
            messages.success(request, "Omega1키을 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.OPCfirstkey == 1:
        messages.error(request, "이미 Omega1키가 있습니다.")

    else:
        messages.error(request, "구매할 수 없습니다.")

    return redirect('core:shop')


def buyOPCsecondkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.OPCsecondkey == 0
        and userkey.OPCfirstkey == 1
    )
    conditionSet2 = (
        coin.purplecoin >= 15
        and coin.pinkcoin >= 15
        and coin.orangecoin >= 15
        and coin.greencoin >= 15
        and coin.bluecoin >= 15
    )

    if conditionSet:
        if conditionSet2:
            userkey.OPCsecondkey += 1
            userkey.save()
            coin.purplecoin -= 15
            coin.pinkcoin -= 15
            coin.orangecoin -= 15
            coin.greencoin -= 15
            coin.bluecoin -= 15
            coin.save()
            messages.success(request, "Omega2키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.OPCfirstkey == 0:
        messages.error(request, "Omega1키가 없습니다")

    elif userkey.OPCsecondkey == 1:
        messages.error(request, "이미 Omega2키가 있습니다.")

    else:
        messages.error(request, "구매할 수 없습니다")

    return redirect('core:shop')


def buyOPCthirdkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.OPCthirdkey == 0
        and userkey.OPCsecondkey == 1
    )
    conditionSet2 = (
        coin.purplecoin >= 30
        and coin.pinkcoin >= 30
        and coin.orangecoin >= 30
        and coin.greencoin >= 30
        and coin.bluecoin >= 30
    )

    if conditionSet or userkey.NPAfifthkey == 1:
        if conditionSet2:
            userkey.OPCthirdkey += 1
            userkey.save()
            coin.purplecoin -= 30
            coin.pinkcoin -= 30
            coin.orangecoin -= 30
            coin.greencoin -= 30
            coin.bluecoin -= 30
            coin.save()
            if userkey.NPAfifthkey == 1:
                userkey.NPAfifthkey -= 1
                userkey.save()
            messages.success(request, "Omega3키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.OPCsecondkey == 0:
        messages.error(request, "Omega2키가 없습니다")

    elif userkey.OPCthirdkey == 1:
        messages.error(request, "이미 Omega3키가 있습니다.")

    else:
        messages.error(request, "구매할 수 없습니다.")

    return redirect('core:shop')


def buyOPCfourthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.OPCfourthkey == 0
        and userkey.OPCthirdkey == 1
    )
    conditionSet2 = (
        coin.purplecoin >= 30
        and coin.pinkcoin >= 30
        and coin.orangecoin >= 30
        and coin.greencoin >= 30
        and coin.bluecoin >= 30
    )

    if conditionSet:
        if conditionSet2:
            userkey.OPCfourthkey += 1
            userkey.save()
            coin.purplecoin -= 30
            coin.pinkcoin -= 30
            coin.orangecoin -= 30
            coin.greencoin -= 30
            coin.bluecoin -= 30
            coin.save()
            messages.success(request, "Omega4키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.OPCthirdkey == 0:
        messages.error(request, "Omega3키가 없습니다")

    elif userkey.OPCfourthkey == 1:
        messages.error(request, "이미 Omega4키가 있습니다.")

    else:
        messages.error(request, "구매할 수 없습니다. ")

    return redirect('core:shop')


def buyOPCfifthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.OPCfifthkey == 0
        and userkey.OPCfourthkey == 1
    )
    conditionSet2 = (
        coin.purplecoin >= 60
        and coin.pinkcoin >= 60
        and coin.orangecoin >= 60
        and coin.greencoin >= 60
        and coin.bluecoin >= 60
    )

    if conditionSet:
        if conditionSet2:
            userkey.OPCfifthkey += 1
            userkey.save()
            coin.purplecoin -= 60
            coin.pinkcoin -= 60
            coin.orangecoin -= 60
            coin.greencoin -= 60
            coin.bluecoin -= 60
            coin.save()
            messages.success(request, "Omega5키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.OPCfourthkey == 0:
        messages.error(request, "Omega4키가 없습니다")

    elif userkey.OPCfifthkey == 1:
        messages.error(request, "이미 Omega5키가 있습니다.")

    else:
        messages.error(request, "구매할 수 없습니다.")

    return redirect('core:shop')


def buyOPCsixthkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.OPCsixthkey == 0
        and userkey.OPCfifthkey == 1
    )
    conditionSet2 = (
        coin.purplecoin >= 60
        and coin.pinkcoin >= 60
        and coin.orangecoin >= 60
        and coin.greencoin >= 60
        and coin.bluecoin >= 60
    )

    if conditionSet:
        if conditionSet2:
            userkey.OPCsixthkey += 1
            userkey.save()
            coin.purplecoin -= 60
            coin.pinkcoin -= 60
            coin.orangecoin -= 60
            coin.greencoin -= 60
            coin.bluecoin -= 60
            coin.save()
            messages.success(request, "Omega6키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.OPCfifthkey == 0:
        messages.error(request, "Omega5키가 없습니다")

    elif userkey.OPCsixthkey == 1:
        messages.error(request, "이미 Omega6키가 있습니다.")

    else:
        messages.error(request, "구매할 수 없습니다.")

    return redirect('core:shop')


def buyOPCseventhkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.OPCseventhkey == 0
        and userkey.OPCsixthkey == 1
    )
    conditionSet2 = (
        coin.purplecoin >= 60
        and coin.pinkcoin >= 60
        and coin.orangecoin >= 60
        and coin.greencoin >= 60
        and coin.bluecoin >= 60
    )

    if conditionSet:
        if conditionSet2:
            userkey.OPCseventhkey += 1
            userkey.save()
            coin.purplecoin -= 60
            coin.pinkcoin -= 60
            coin.orangecoin -= 60
            coin.greencoin -= 60
            coin.bluecoin -= 60
            coin.save()
            messages.success(request, "Omega7키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.OPCsixthkey == 0:
        messages.error(request, "Omega6키가 없습니다")

    elif userkey.OPCseventhkey == 1:
        messages.error(request, "이미 Omega7키가 있습니다.")

    else:
        messages.error(request, "구매할 수 없습니다.")

    return redirect('core:shop')


def buySSkey(request):
    userkey = UserKey.objects.get(user=request.user)
    coin = Coin.objects.get(user=request.user)
    jprofile = JProfile.objects.get(user=request.user)
    conditionSet = (
        userkey.SSkey == 0
        and userkey.OPCseventhkey == 1
    )
    conditionSet2 = (
        coin.purplecoin >= 50
        and coin.pinkcoin >= 50
        and coin.orangecoin >= 50
        and coin.greencoin >= 50
        and coin.bluecoin >= 50
    )

    if conditionSet:
        if conditionSet2:
            userkey.SSkey += 1
            userkey.save()
            coin.purplecoin -= 50
            coin.pinkcoin -= 50
            coin.orangecoin -= 50
            coin.greencoin -= 50
            coin.bluecoin -= 50
            coin.save()
            messages.success(request, "SS키를 샀어요")
        else:
            messages.error(request, "코인이 부족합니다")

    elif userkey.OPCseventhkey == 0:
        messages.error(request, "Omega7키가 없습니다")

    elif userkey.SSkey == 1:
        messages.error(request, "이미 SS키가 있습니다.")

    else:
        messages.error(request, "구매할 수 없습니다.")

    return redirect('core:shop')


# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
#
# @register_job(scheduler, "cron", hour=23, minute=59, second=55)
# def cron_job2():
#     num_progressivism = JProfile.objects.filter(political_orientation='progressivism').count()
#     num_centrism = JProfile.objects.filter(Q(political_orientation='centrism') | Q(political_orientation='default')).count()
#     num_conservatism = JProfile.objects.filter(political_orientation='conservatism').count()
#     classification_progressivism = Classification.objects.get(political_orientation='progressivism')
#     classification_progressivism.numberOfUser = num_progressivism
#     classification_progressivism.save()
#     classification_centrism = Classification.objects.get(political_orientation='centrism')
#     classification_centrism.numberOfUser = num_centrism
#     classification_centrism.save()
#     classification_conservatism = Classification.objects.get(political_orientation='conservatism')
#     classification_conservatism.numberOfUser = num_conservatism
#     classification_conservatism.save()
#     db.connections.close_all()
#
# register_events(scheduler)
# scheduler.start()
