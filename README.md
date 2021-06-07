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
**조선 시대 게시글 예시**  

![random_nickname](https://user-images.githubusercontent.com/82914197/120980107-3ce96680-c7b1-11eb-94e2-d52deb64c05a.png)  

## 화면 상단에 실시간 신규회원의 정치성향 증감률 확인 기능
- 조선 시대 품계를 모델로 한 레벨링
- 상점과 아이템
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
