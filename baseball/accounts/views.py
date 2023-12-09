from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import SignupForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages

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