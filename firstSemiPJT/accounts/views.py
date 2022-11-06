from django.shortcuts import render

# Create your views here.

# 회원 가입
def signup(request):
    return render(request, 'accounts/signup.html')