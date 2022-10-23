from django.shortcuts import redirect, render
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Profile
from django.contrib.auth import login as auth_login


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
            return redirect('reviews:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)