from django.shortcuts import render, get_object_or_404, redirect
from .forms import InformationForm
from .models import Information
from django.views.decorators.http import require_safe
from django.contrib.auth.decorators import login_required

# Create your views here.

# 글 목록
def index(request):
    articles = Information.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'information/index.html', context)

# 글 조회
def detail(request, pk):
    article = get_object_or_404(Information, pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'information/detail.html', context)

# 글 작성
@login_required
def create(request):
    if request.method == 'POST':
        article_form = InformationForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('information:index')
    else:
        article_form = InformationForm()
    context = {
        'article_form' : article_form
    }
    return render(request, 'information/form.html', context)

# 글 수정
@login_required
def update(request, pk):
    article = get_object_or_404(Information, pk)
    if request.method == 'POST':
        article_form = InformationForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('information:detail', article.pk)
    else:
        article_form = InformationForm(instance=article)
    context = {
        'article_form' : article_form
    }
    return render(request, 'information/form.html', context)

# 글 삭제
def delete(request, pk):
    article = Information.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('information:index')
    context = {
        'article' : article
    }
    return render(request, 'information/index.html', context)