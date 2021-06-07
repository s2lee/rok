## :pencil: Table of Contents
- [Part 1. 프로젝트 소개](#1-프로젝트-소개)
- [Part 2. 사용 기술 스택](#2-사용-기술-스택)
- [Part 3. 주요 기능](#3-주요-기능)
  - 조선 시대에 게시글, 댓글 작성시 랜덤닉네임 부여 기능
  - 화면 상단에서 전체회원의 정치성향 증감률을 실시간 확인하는 기능
  - 조선 시대 품계를 모델로 한 레벨링
  - 상점과 아이템  
- [Part 4. 기본 기능](#4-기본-기능)
  - 로그인
  - 회원가입
  - 커뮤니티 게시판과 댓글, 답글, TOP3 댓글 고정 기능
  - 게시글 추천 및 조선시대 창과 방패 기능
  - 프로필 보기 / 수정
  - 스크랩
  - 인벤토리
- [Part 5. 주요 이슈](#5-주요-이슈)
- [Part 6. 보완할 점](#6-보완할-점)

# 1. 프로젝트 소개
**The Rank of Korea (2021)**
  
  
"내가 조선시대로 돌아가 정치를 한다면?"을 주제로 한 언론형 커뮤니티플랫폼입니다.   

기본적으로 Django 웹앱 기반 프로젝트입니다.

**https://therok.net**

# 2. 사용 기술 스택
- Django
- Ajax
- Python
- JavaScript
- AWS EC2(Windows)
- PyCharm, Visual Studio Code, Windows
# 3. 주요 기능
## 조선 시대에 게시글, 댓글 작성시 랜덤닉네임 부여 기능  
조선 시대를 제외한 게시판에서는 회원가입 때 작성한 닉네임을 사용하지만 조선 시대에서는 익명성을 보장하기 위해 게시글이나 댓글, 답글을 작성할 때 무작위 닉네임을 부여합니다.  

**1. 무작위 닉네임은 형용사 + 명사를 조합해서 사용합니다.**  
**2. make_nickname 함수를 만들어 adjective.txt 와 word.txt에서 단어를 가져와 닉네임을 만들고 리턴합니다.**  
```python
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
```

**3. 게시글과 댓글, 답글을 작성할 때 anonymous 값을 넣어줍니다. (게시글 예시)**  
```python
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
```  
**<p align="center"><조선 시대 게시글 예시></p>**
<p align="center">
  <img width="100%" height="100%" src="https://user-images.githubusercontent.com/82914197/120980107-3ce96680-c7b1-11eb-94e2-d52deb64c05a.png">
</p>
  
  
## 화면 상단에 실시간 신규회원의 정치성향 증감률 확인 기능  
플랫폼 성격상 특정 정치 성향에 편중 되지 않기 위해 전체 회원의 실시간 정치성향분포를 나타내기로 하였습니다. 증감률은 어제 23:59:55초의 회원 정보를 저장한 후 오늘의 증감분을 계산 후 출력하였습니다.  
원하는 시간에 Python script 를 실행하기 위해 라이브러리 APScheduler를 사용하였습니다.  
```python
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, "cron", hour=23, minute=59, second=55)
def cron_job2():
    num_progressivism = JProfile.objects.filter(political_orientation='progressivism').count()
    num_centrism = JProfile.objects.filter(Q(political_orientation='centrism') | Q(political_orientation='default')).count()
    num_conservatism = JProfile.objects.filter(political_orientation='conservatism').count()
    classification_progressivism = Classification.objects.get(political_orientation='progressivism')
    classification_progressivism.numberOfUser = num_progressivism
    classification_progressivism.save()
    classification_centrism = Classification.objects.get(political_orientation='centrism')
    classification_centrism.numberOfUser = num_centrism
    classification_centrism.save()
    classification_conservatism = Classification.objects.get(political_orientation='conservatism')
    classification_conservatism.numberOfUser = num_conservatism
    classification_conservatism.save()
    db.connections.close_all()

register_events(scheduler)
scheduler.start()
```  
**<p align="center"><웹 화면 상단></p>**
<p align="center">
  <img width="100%" height="100%" src="https://user-images.githubusercontent.com/82914197/121003502-93ae6a80-c7c8-11eb-8279-b8b8cba4184f.PNG">
</p>  

**<p align="center"><모바일 화면 상단></p>** 
<p align="center">
  <img width="25%" height="25%" src="https://user-images.githubusercontent.com/82914197/121003564-a45ee080-c7c8-11eb-8e4a-9863ad661a3c.PNG">
</p>
  
  
## 조선 시대 품계를 모델로 한 레벨링  
  
  
## 상점과 아이템
# 4. 기본 기능
- 로그인
- 회원가입
- 프로필 보기 / 수정
- 스크랩
- 인벤토리
- 커뮤니티 게시판과 댓글, 답글, TOP3 댓글 고정 기능
- 게시글 추천 및 조선시대 창과 방패 기능
# 5. 주요 이슈
- debug toolbar로 쿼리 중복최소화 제거하고
- 게시글 도배 방지
- manytomany 필드 버튼 누르면 페이지 다시 가져와서 로딩가지니깐 spa로 ajax 비동기 구현
- top 고정배너에 정치선호분포 포현 이슈(celery, threading, schedule, apschedule 중에서 apschedule 사용)
# 6. 보완할 점
