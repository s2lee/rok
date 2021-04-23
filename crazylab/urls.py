from django.urls import path
from django.conf.urls import url
from .views import (
    PublicIdeaListView,
    TodayIdeaListView,
    CrazyIdeaListView,
    crazylab_detail,
    post_publicidea,
    post_todayidea,
    post_crazyidea,
    add_star,
    recommend,
    scrap,
    user_scrap,
    up_comment,
    accuse_post,
    accuse_comment,
)

app_name = 'crazylab'

urlpatterns = [
    path('publicidea', PublicIdeaListView.as_view(), name = 'publicidea_list'),
    path('todayidea', TodayIdeaListView.as_view(), name = 'todayidea_list'),
    path('crazyidea', CrazyIdeaListView.as_view(), name = 'crazyidea_list'),    
    path('<int:pk>', crazylab_detail, name="crazylab_detail"),
    path('publicidea/post', post_publicidea, name='post_publicidea'),
    path('todayidea/post', post_todayidea, name='post_todayidea'),
    path('crazyidea/post', post_crazyidea, name='post_crazyidea'),
    path('recommend', recommend, name='recommend'),
    path('add_star', add_star, name='add_star'),
    path('scrap', scrap, name='scrap'),
    path('user_scrap/<int:pk>', user_scrap, name='user_scrap'),
    path('up_comment', up_comment, name='up_comment'),
    path('accuse_post', accuse_post, name='accuse_post'),
    path('accuse_comment', accuse_comment, name='accuse_comment'),
]
