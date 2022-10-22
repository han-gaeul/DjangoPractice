from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import CommentForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# 리뷰 목록
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/index.html', context)

# 리뷰 조회
def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'review' : review,
        'comments' : review.comment_set.all(),
        'comment_form' : comment_form
    }
    return render(request, 'reviews/detail.html', context)

# 리뷰 작성
@login_required
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, '글이 작성 되었습니다.')
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    context = {
        'review_form' : review_form
    }
    return render(request, 'reviews/form.html', context)

# 리뷰 수정
@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, '글이 수정 되었습니다.')
            return redirect('reviews:detail', review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        'review_form' : review_form
    }
    return render(request, 'reviews/form.html', context)

# 리뷰 삭제
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('reviews:index')
    context = {
        'review' : review
    }
    return render(request, 'reviews/index.html', context)