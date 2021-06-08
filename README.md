## :pencil: Table of Contents
- [Part 1. 프로젝트 소개](#1-프로젝트-소개)
- [Part 2. 사용 기술 스택](#2-사용-기술-스택)
- [Part 3. 주요 기능](#3-주요-기능)
  - [조선 시대에서 글을 작성할 때마다 랜덤 닉네임을 부여하는 기능](#조선-시대에서-글을-작성할-때마다-랜덤-닉네임을-부여하는-기능)
  - [화면 상단에서 전체회원의 정치성향 증감률을 실시간 확인하는 기능](#화면-상단에서-전체회원의-정치성향-증감률을-실시간-확인하는-기능)
  - [조선 시대 품계를 모델로 한 레벨링](#조선-시대-품계를-모델로-한-레벨링)
  - [상점과 아이템](#상점과-아이템)  
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
## 조선 시대에서 글을 작성할 때마다 랜덤 닉네임을 부여하는 기능  
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
  <img width="90%" height="90%" src="https://user-images.githubusercontent.com/82914197/120980107-3ce96680-c7b1-11eb-94e2-d52deb64c05a.png">
</p>
  
  
## 화면 상단에서 전체회원의 정치성향 증감률을 실시간 확인하는 기능  
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
회원가입을 하면 조선 시대 품계 종9품의 기자로 시작합니다. 평소 관심사에 대한 글을 쓰면서 품계 상승을 할 수있습니다. 품계는 종9품부터 정1품까지 나아 갈 수 있고 정1품이 되면 랭커가 될 수 있는 자격이 주어집니다. 종6품이상이 되면 전직 부서를 정할 수 있습니다. 부서의 종류는 공조, 이조, 사간원, 사헌부, 의금부가 있습니다. 부서별로 주어지는 역할과 레벨링 조건이 다릅니다.  
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
상점에는 조선 시대에서 사용할 수 있는 아이템(창, 방패, 칼, 갑옷), 부서마다 다른 스페셜 아이템, 레벨업 재료인 증서와 키를 구매할 수 있습니다. 창과 방패는 게시글, 댓글, 답글에 대한 추천, 반대 효과가 있고 칼과 갑옷은 부적절한 유저에 대한 신고기능과 신고방어 효과가 있습니다.    

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
**4. 새로고침이 없는 버튼클릭을 위해 Ajax를 사용하여 구현하였습니다.**
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
  <img width="100%" height="100%" src="https://user-images.githubusercontent.com/82914197/121124987-c4da7980-c860-11eb-9ef2-e61b2cfb9b8f.PNG">
</p>  
  
  
**<p align="center"><게시글에 창 사용></p>**
<p align="center">
  <img width="100%" height="100%" src="https://user-images.githubusercontent.com/82914197/121124995-c6a43d00-c860-11eb-8c80-3952907cca56.PNG">
</p>    
  
 ## 커뮤니티 게시판과 댓글  
커뮤니티 게시판과 댓글, 답글을 구현해 보았습니다. Debug toolbar를 사용하여 쿼리가 중복되는 부분을 찾고 중복을 최소화 했습니다.  
  
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
        context['tops'] = Post.objects.filter(category__name='공익아이디어').annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:5]

        return context
```  
**2. 댓글과 답글을 불러올 때 ForeignKey관계와 ManyToMany 관계에 있는 쿼리셋의 중복을 최소화하였습니다.**  
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
    
# 4. 기본 기능
### 로그인
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
