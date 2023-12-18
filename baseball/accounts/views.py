from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import SignupForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
import os
import requests
from django.http import HttpResponse
from accounts.models import MyUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
        
    else:
        form = SignupForm()

        
    return render(request, 'registration/signup.html', {'form':form})


class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        # 일회용 메시지 작성
        messages.info(self.request, '암호 변경을 완료했습니다.')
        return super().form_valid(form)       
    
    
from dotenv import load_dotenv
load_dotenv()

def kakao_login(request):
    client_id =  os.getenv('REST_API_KEY')
    redirect_uri =  os.getenv('REDIRECT_URI')
    print(f"client_id: {client_id}")
    print(f"redirect_uri: {redirect_uri}")
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
        )

class KakaoException(Exception):
    pass

def kakao_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get('REST_API_KEY')
        redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback"
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
        )
        
        token_json = token_request.json()
        error = token_json.get("error", None)
        
        if error is not None:
            raise KakaoException()
        
        access_token = token_json.get("access_token")
        profile_request = requests.get("https://kapi.kakao.com/v2/user/me", headers={'Authorization':
            f"Bearer {access_token}"},
            )
        
        profile_json = profile_request.json() 
        user_id = profile_json.get('id')
        #email = profile_json.get("kakao_account").get("email")
        properties = profile_json.get("properties")
        nickname = properties.get("nickname")
        profile_image = properties.get("profile_image", "")
        
        print('username',nickname)
 
        user = MyUser.objects.create(
            username = nickname,
            avatar=profile_image,
        )
        
    
        
        login(request, user)
        
        if request.user.is_authenticated:
            return redirect('profile')
        
    except KakaoException:
        return HttpResponse("Fail")
        