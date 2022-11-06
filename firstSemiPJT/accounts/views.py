from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileForm
from .models import Profile
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.

# 회원 가입
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        profile = Profile()
        if form.is_valid():
            user = form.save()
            profile.user = user
            profile.save()
            auth_login(request, user)
            return redirect('information:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

# 로그인
def login(request):
    if request.user.is_authenticated:
        return redirect('information:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'information:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('information:index')

# 비밀번호 변경
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('information:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)

# 회원 정보
@login_required
def profile(request):
    user = request.user
    articles = user.article_set.all()
    profile = user.profile_set.all()[0]
    context = {
        'articles' : articles,
        'profile' : profile,
    }
    return render(request, 'accounts/profile.html', context)

# 프로필 수정
@login_required
def profile_update(request):
    user = get_user_model().objects.get(pk=request.user.pk)
    current_user = user.profile_set.all()[0]
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, isinstance=current_user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(isinstance=current_user)
    context = {
        'profile_form' : form,
    }
    return render(request, 'accounts/profile_update.html', context)

# 팔로우
@login_required
def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect('accounts:profile', pk)