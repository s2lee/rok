## :pencil: Table of Contents
- [Part 1. 프로젝트 소개](#1-프로젝트-소개)
- [Part 2. 사용 기술 스택](#2-사용-기술-스택)
- [Part 3. 주요 기능](#3-주요-기능)
  - 조선시대에 게시글, 댓글 작성시 랜덤닉네임 부여 기능
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
- 조선시대에 게시글, 댓글 작성시 랜덤닉네임 부여 기능
- 화면 상단에 실시간 신규회원의 정치성향 증감률 확인 기능
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
