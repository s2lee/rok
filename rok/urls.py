"""rok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('reality/', include('reality.urls')),
    path('joseon/', include('joseon.urls', namespace='joseon')),
    path('crazylab/', include('crazylab.urls')),
    path('register/', user_views.register, name='register'),
    path('register_confirm/', user_views.register_confirm, name='register_confirm'),
    path('HowToPlay/', user_views.HowToPlay, name='HowToPlay'),
    path('profile/', user_views.profile, name='profile'),
    path('jprofile/', user_views.jprofile, name='jprofile'),
    path('inventory/', user_views.inventory, name='inventory'),
    path('view_scrap/', user_views.view_scrap, name='view_scrap'),
    path('view_ranking/', user_views.view_ranking, name='view_ranking'),
    path('author/<str:nickname>', user_views.get_user_profile, name='get_user_profile'),
    path('profile_update', user_views.Updateprofile, name='profile_update'),
    path('jprofile_update', user_views.Updatejprofile, name='jprofile_update'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
