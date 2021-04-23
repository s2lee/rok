from django.urls import path, include
from django.conf.urls import url
from .views import (
    NovelListView,
    PoetryListView,
    LetterListView,
    reality_detail,
    post_novel,
    post_poetry,
    post_letter,
    recommend,
    scrap,
    user_scrap,
    up_comment,
    accuse_post,
    accuse_comment,
)

app_name = 'reality'

urlpatterns = [
    path('novel', NovelListView.as_view(), name = 'novel_list'),
    path('poetry', PoetryListView.as_view(), name = 'poetry_list'),
    path('letter', LetterListView.as_view(), name = 'letter_list'),
    path('<int:pk>', reality_detail, name='reality_detail'),
    path('novel/post', post_novel, name='post_novel'),
    path('poetry/post', post_poetry, name='post_poetry'),
    path('letter/post', post_letter, name='post_letter'),
    path('recommend', recommend, name='recommend'),
    path('scrap', scrap, name='scrap'),
    path('user_scrap/<int:pk>', user_scrap, name='user_scrap'),
    path('up_comment', up_comment, name='up_comment'),
    path('accuse_post', accuse_post, name='accuse_post'),
    path('accuse_comment', accuse_comment, name='accuse_comment')
]
