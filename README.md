## :pencil: Table of Contents
- [Part 1. 프로젝트 소개](#1-프로젝트-소개)
- [Part 2. 사용 기술 스택](#2-사용-기술-스택)
- [Part 3. 주요 기능](#3-주요-기능)
  - [조선 시대에서 글을 작성할 때마다 랜덤 닉네임을 부여하는 기능](#조선-시대에서-글을-작성할-때마다-랜덤-닉네임을-부여하는-기능)
  - [화면 상단에서 전체회원의 정치성향 증감률을 실시간 확인하는 기능](#화면-상단에서-전체회원의-정치성향-증감률을-실시간-확인하는-기능)
  - [조선 시대 품계를 모델로 한 레벨링](#조선-시대-품계를-모델로-한-레벨링)
  - [상점과 아이템](#상점과-아이템)  
  - [커뮤니티 게시판과 댓글](#커뮤니티-게시판과-댓글)
- [Part 4. 주요 이슈](#4-주요-이슈)  
  - [조선 시대에서 랜덤 닉네임을 댓글 또는 답글에 부여하는 문제](#조선-시대에서-랜덤-닉네임을-댓글-또는-답글에-부여하는-문제)  
  - [댓글 작성 시 manytomany필드가 많아지면서 화면 로딩 시간이 길어지는 문제](#댓글-작성-시-manytomany필드가-많아지면서-화면-로딩-시간이-길어지는-문제)  
  - [실시간 전체회원 정치성향 증감률 구하는 문제](#실시간-전체회원-정치성향-증감률-구하는-문제)  
- [Part 5. 보완할 점](#5-보완할-점)
  
<br/><br/><br/>
# 1. 프로젝트 소개
**The Rank of Korea (2021)**
  
"**내가 조선 시대로 돌아가 정치를 한다면?**"을 주제로 한 **언론형 커뮤니티플랫폼**입니다. 플랫폼은 기본적인 커뮤니티 형태(게시글, 댓글, 답글)에 오락요소(회원 레벨링, 사용자 아이템)를 더한 구성을 하였습니다.    

기본적으로 Django 웹앱 기반 프로젝트입니다.

:exclamation: version2로 바뀜 --> **https://therok.net**

# 2. 사용 기술 스택
- **Front - Javascript, Ajax**
- **Back - Python, Django**
- **Server - AWS[EC2(windows)]**
- **PyCharm, Visual Studio Code**
# 3. 주요 기능
## 조선 시대에서 글을 작성할 때마다 랜덤 닉네임을 부여하는 기능  
조선 시대를 제외한 게시판에서는 회원가입 때 작성한 닉네임을 사용하지만, 조선 시대에서는 익명성을 보장하기 위해 게시글이나 댓글, 답글을 작성할 때 무작위 닉네임을 부여합니다.  

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
  <img src="https://user-images.githubusercontent.com/82914197/120980107-3ce96680-c7b1-11eb-94e2-d52deb64c05a.png">
</p>
  
  
## 화면 상단에서 전체회원의 정치성향 증감률을 실시간 확인하는 기능  
플랫폼 성격상 특정 정치 성향에 편중되지 않기 위해 전체 회원의 실시간 정치성향분포를 나타내기로 하였습니다. 증감률은 어제 23:59:55 초의 회원 정보를 저장한 후 오늘의 증감분을 계산 후 출력하였습니다.  
원하는 시간에 Python script를 실행하기 위해 라이브러리 APScheduler를 사용하였습니다.  
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
  <img src="https://user-images.githubusercontent.com/82914197/121003502-93ae6a80-c7c8-11eb-8279-b8b8cba4184f.PNG">
</p>  

**<p align="center"><모바일 화면 상단></p>** 
<p align="center">
  <img width="25%" height="25%" src="https://user-images.githubusercontent.com/82914197/121003564-a45ee080-c7c8-11eb-8e4a-9863ad661a3c.PNG">
</p>
  
  
## 조선 시대 품계를 모델로 한 레벨링  
회원가입을 하면 조선 시대 품계 종9품의 기자로 시작합니다. 평소 관심사에 대한 글을 쓰면서 품계 상승을 할 수 있습니다. 품계는 종9품부터 정1품까지 나아 갈 수 있고 정1품이 되면 랭커가 될 수 있는 자격이 주어집니다. 종6품 이상이 되면 전직 부서를 정할 수 있습니다. 부서의 종류는 공조, 이조, 사간원, 사헌부, 의금부가 있습니다. 부서별로 주어지는 역할과 레벨링 조건이 다릅니다.  
단순 조건문으로 조건이 만족하면 레벨업을 수행하는 함수를 작성하였습니다.
```python
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
    
    if conditionSet:
        jprofile.position = '정언'
        jprofile.levels -= 1
        jprofile.save()
        certificate.BAIcertificate -= 1
        certificate.save()
    else:
        if jprofile.levels == 12 and certificate.BAIcertificate < 1:
            messages.error(request, "증서가 부족합니다")
```

  
## 상점과 아이템  
상점에는 조선 시대에서 사용할 수 있는 아이템(창, 방패, 칼, 갑옷), 부서마다 다른 스페셜 아이템, 레벨업 재료인 증서와 키를 구매할 수 있습니다. 창과 방패는 게시글, 댓글, 답글에 대한 추천, 반대 효과가 있고 칼과 갑옷은 부적절한 사용자에 대한 신고기능과 신고방어 효과가 있습니다.    

**1. 상점에서 창을 구매하는 함수 입니다.**  
```python
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
```  

**2. 게시글에 창을 사용하는 함수입니다.**
```python
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
```    
**3. 창 버튼 HTML 구성입니다.**
```html
<form action="{% url 'joseon:add_spear' %}" method='POST'>
  {% csrf_token %}
  {% if request.user in post.spear.all %}
    <button type="submit" id="spear" value="{{ post.id }}" class="joseon_detail_btn">
			<img src="{% static 'images/spear-red.png' %}" alt="" title="창">
		</button>
		<span class="joseon_detail-btn-count" style="color:#ff0000;">{{ get_total_spear }}</span>
  {% else %}
    <button type="submit" id="spear" value="{{ post.id }}" class="joseon_detail_btn">
			<img src="{% static 'images/spear-detail.png' %}" alt="" title="창">
		</button>
		<span class="joseon_detail-btn-count">{{ get_total_spear }}</span>
  {% endif %}
</form>
```  
**4. 새로고침 없는 버튼클릭을 위해 Ajax를 사용하여 구현하였습니다.**
```javascript
$(document).on('click', '#spear', function(event){
	    event.preventDefault();
	    var pk = $(this).attr('value');
	    $.ajax({
	      type: 'POST',
	      url : '{% url "joseon:add_spear" %}',
	      data: {'id':pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
	      dataType: 'json',
	      success: function(response){
	        $('#spear-section').html(response['form']);
	      },
	      error: function(response, e){
	        alert("아이템 사용을 실패하였습니다.");
	      },
	    });
	  });
```  
**<p align="center"><상점 화면></p>**
<p align="center">
  <img src="https://user-images.githubusercontent.com/82914197/121124987-c4da7980-c860-11eb-9ef2-e61b2cfb9b8f.PNG">
</p>  
  
  
**<p align="center"><게시글에 창 사용></p>**
<p align="center">
  <img src="https://user-images.githubusercontent.com/82914197/121124995-c6a43d00-c860-11eb-8c80-3952907cca56.PNG">
</p>    
  
 ## 커뮤니티 게시판과 댓글  
커뮤니티 게시판과 댓글, 답글을 구현해 보았습니다. Debug toolbar를 사용하여 쿼리가 중복되는 부분을 찾고 중복을 최소화했습니다.  
  
**1. 게시글을 불러올 때 OneToOne관계와 ForeignKey관계에 있는 쿼리셋의 중복을 최소화하였습니다.**  
```python
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
        context['tops'] = Post.objects.filter(category__name='공익아이디어').annotate(
                          comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:5]

        return context
```  
**2. 댓글과 답글을 불러올 때 ForeignKey관계와 ManyToMany관계에 있는 쿼리셋의 중복을 최소화하였습니다.**  
```python
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
```  
**<p align="center"><댓글 구성 예시></p>**
<p align="center">
  <img src="https://user-images.githubusercontent.com/82914197/121182092-b2cafc00-c89d-11eb-8dfc-2fb29f70e481.PNG">
</p>   

# 4. 주요 이슈
## 조선 시대에서 랜덤 닉네임을 댓글 또는 답글에 부여하는 문제  
조선 시대에서 글을 쓸 때는 익명성을 보장하기 위해 고정 닉네임을 사용하는 것이 아니라 랜덤 닉네임을 그때마다 생성하여 사용하기로 했습니다. 게시글을 포스트 할 때는 Post model에 anonymous 속성을 추가하여 랜덤 닉네임을 생성해서 넣어주면 포스트마다 랜덤 닉네임이 부여되었습니다. 하지만 해당 게시글의 댓글을 쓸 때 문제가 생깁니다.  

**문제**
1. 예를 들어 사용자 A가 9번 게시글에 댓글을 쓰면 Post model에 anonymous 속성에  랜덤닉네임이 생성된 후 부여됩니다.    
2. 만약에 사용자 A가 9번 게시글에 댓글을 한 번 더 쓰면 랜덤 닉네임을 또다시 생성되어 9번 게시글에서 사용자 A의 랜덤닉네임이 변경되었습니다.  
3. 제가 하고자 했던 바는 사용자 A가 9번 게시글에서 댓글을 쓸 때는 1번에서 만들어진 랜덤 닉네임을 계속 사용하는 것이었습니다.        

**해결**
1. Post model에 nickname_check 속성을 추가해서 ManyToMany필드로 만듭니다.  
2. 이 속성에 처음에 댓글을 달면서 새로운 랜덤 닉네임을 가지면 nickname_check으로 체크를 해주고 그다음에 댓글 쓸 때는 새로운 닉네임을 부여하지 않고 처음의 랜덤 닉네임을 가져오게 하였습니다.
```python
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
```
## 댓글 작성 시 manytomany필드가 많아지면서 화면 로딩 시간이 길어지는 문제  
**문제**  
처음 댓글단 구성에 추천/반대 기능을 ManyToMany필드로 만들었을 때 구현하는 데 신경을 쓰느라 로딩 시간은 생각하지 못하였습니다. 그런데 어느 정도 구현하고 댓글에서 추천/반대를 눌러보니 페이지가 새로 고침 되면서 시간이 상당히 걸렸습니다. 이 로딩 시간이 댓글이 많아질수록 로딩 시간이 길어졌습니다. 유튜브만 사용해봐도 댓글에 있는 '좋아요/싫어요' 를 눌렀을 때 로딩 체감시간이 전혀 불편하지 않은데 제가 만든 추천/반대는 상식을 벗어나는 로딩속도를 보여주고 있었습니다.  
**<p align="center"><Debug toolbar 화면></p>**
<p align="center">
  <img width="100%" height="100%" src="https://user-images.githubusercontent.com/82914197/121477171-7b299480-ca02-11eb-83a2-561529f12f14.JPG">
</p>  

**해결방법**  
쿼리 중복을 최소한 한다고는 했지만 긴 로딩속도에 대해 다른 해결 방법을 찾아야 했습니다. 추천 버튼을 누를 때 새로 고침이 계속 발생하니까 여기서부터 방법을 찾으면 될 것 같아서 새로 고침을 안 하는 방향으로 해결 방법을 찾아보았습니다. 검색하던 중 Ajax를 사용해서 비동기적인 처리를 하면 페이지를 새로 고침 하지 않고 데이터만 주고받을 수 있다고 하여 추천/반대 기능뿐만 아니라 댓글, 답글을 작성하는 것과 아이템을 사용하는 모든 처리에서 비동기화를 구현하였습니다.  
```python
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
```

## 실시간 전체회원 정치성향 증감률 구하는 문제  
화면 상단에 전체 회원 정치성향 증감률을 실시간 표현하기 위해 어제의 데이터를 매일 일정한 시간에 저장할 필요가 있었습니다. 이를 위해서는 매일 일정한 시간에 해당 역할을 하는 함수를 작동시키게끔 하면 된다고 생각하였습니다. 검색해보니 이런 방법에 사용할 수 있는 목록이 celery, threading, schedule, apschedule 정도 있었습니다.  
**1. celery**  
 사실 celery가 가장 이상적인 방법인 것 같았으나 아래 두 이유로 보류
 - celery 4.0부터 윈도우 운영체제를 지원하지 않는 것(물론 windows에서도 gevent 패키지를 설치하고 진행하면 되는 것 같습니다)[2012년산 삼성노트북 사용 중]
 - celery 작동 방법이 조금 더 배경지식이 있어야 정확히 이해하고 사용할 수 있을 것 같다고 생각    
  
**2. threading**  
하나의 작업을 매일 일정 시간에 수행하기에는 적합하였으나 지금은 구현하지 못하였지만, 멀티 쓰레드 프로그램 같은 10개 이상의 작업을 생각하고 있었기 때문에 threading을 이용하여 구현했을 때 파이썬 GIL(Global Interpreter Lock)때문에 원활한 작업이 되지 않을 것 같아서 보류
```python
from threading import Timer
import threading

def timer_delete():
    print('test')
    num_progressivism = JProfile.objects.filter(political_orientation='progressivism').count()
    classification_progressivism = Classification.objects.get(political_orientation='progressivism')
    classification_progressivism.numberOfUser = 2
    classification_progressivism.save()

timer = threading.Timer(1,timer_delete).start()
```  

**3. schedule**  
schedule은 사용하기에 큰 어려움이 없어서 사용하려고 했지만, 작업을 동적으로 추가하거나 유지할 수 없는 단점 때문에 마지막에 찾은 APScheduler를 사용하기로 하였습니다.  
```python
import schedule
import time

def job():
    print("test...")
    num_progressivism = JProfile.objects.filter(political_orientation='progressivism').count()
    classification_progressivism = Classification.objects.get(political_orientation='progressivism')
    classification_progressivism.numberOfUser = 3
    classification_progressivism.save()
schedule.every(5).seconds.do(job)
schedule.every().day.at("20:32").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```
**4. APScheduler 채택**
>I think APScheduler is a tool library that is best used in actual projects.Not only does it allow us to dynamically add and remove our timed tasks in the program, but it also supports persistence, and its persistence scheme supports many forms, including (Memory, MongoDB, SQLAlchemy, Redis, RethinkDB, ZooKeeper), and it can be very good. Integration with some Python frameworks (including asyncio, gevent, Tornado, Twisted, Qt)  
      
출처 : https://www.programmersought.com/article/6923889412/

# 5. 보완할 점  
파이썬으로 *print('Hello world')* 정도의 문법만 익히고 바로 시작한 첫 프로젝트라서 아쉬운 점이 많은 프로젝트입니다. 정말 많은 시행착오와 이슈가 있었는데 Github의 존재도 프로젝트를 마무리할 때부터 알게 되어서 소중한 이슈들을 다 기록하지는 못하였습니다. 다행히 주요 이슈들은 스크린샷으로 찍어놔서 Readme에 기록할 수 있었습니다.  

**보완**  
- 구글링을 하던 중에 Rest API, Django REST framework가 있고 현업에서 많이 쓰인다는 것을 알게 되었습니다. Rest API에 관해 공부하고 프로젝트를 좀더 Restful하게 만들어 봐야겠습니다.  
- 구현에만 초점을 맞추다 보니 개발의 유지보수, 확장성을 신경 쓰지 않은 것 같습니다. 반복, 중복되는 코드를 줄여보고 좀 더 Pythonic한 코드로 다시 빌드업해 봐야겠습니다.  
- 서비스를 AWS로 배포하면서 네트워크 지식이 많이 부족함을 알 수 있었습니다. '왜 Nginx, uWSGI 좋은 선택지가 될 수 있는지', 'Nginx, uWSGI의 원리와 사용방법' 등을 정확히 이해하고 Ubuntu 환경에서 다시 배포해 봐야겠습니다.
