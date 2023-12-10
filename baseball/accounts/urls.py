from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',views.signup, name='signup'),
    path('password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
    path('login/kakao/',views.kakao_login, name='kakao-login'),
    path('login/kakao/callback/',views.kakao_callback, name='kakao-callback'),
]
