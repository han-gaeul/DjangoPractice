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