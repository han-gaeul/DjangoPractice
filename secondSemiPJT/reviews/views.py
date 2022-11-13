import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.views.decorators.http import require_safe
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

# 글 목록
@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/index.html', context)

# 글 작성
@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    context = {
        'form' : form
    }
    return render(request, 'reviews/create.html', context)

# 글 조회
def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()
    context = {
        'review' : review,
        'comment_form' : comment_form
    }
    return render(request, 'reviews/detail.html', context)
    # review = Review.objects.get(pk=review_pk)
    # comment_form = CommentForm()
    # comment = Comment.objects.filter(review=review_pk).order_by('created_at')
    # comment_count = comment.exclude(delete()).count()
    # context = {
    #     'review' : review,
    #     'comment_form' : comment_form,
    #     'comments' : comment,
    #     'comment_count' : comment_count,
    # }
    # return render(request, 'reviews/detail.html', context)

# 글 수정
@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:detail', review_pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form' : form
    }
    return render(request, 'reviews/update.html', context)

# 글 삭제
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('reviews:index')


# 댓글 작성
@login_required
def add_comment(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('reviews:detail', review_pk)
    else:
        comment_form = CommentForm()
    context = {
        'comment_form' : comment_form
    }
    return render(request, 'reviews/add_comment.html', context)

    # review = Review.objects.get(pk=review_pk)
    # comment_form = CommentForm(request.POST)
    # user = request.POST.get('user')
    # content = request.POST.get('content')
    # if content:
    #     comment = Comment.objects.create(review=review, content=content, user=user)
    #     comment_count = Comment.objects.filter(post=review_pk).exclude(deleted=True).count()
    #     review.comments = comment_count
    #     review.save()
    #     data = {
    #         'user' : user,
    #         'content' : content,
    #         'created_at' : '방금 전',
    #         'comment_count' : comment_count,
    #         'comment_id' : comment.id,
    #     }
    #     if request.user == review.user:
    #         data['self_comment'] = '(작성자)'
    #     return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")

# 댓글 삭제
def delete_comment(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('reviews:detail', review_pk)

    # review = Review.objects.get(pk=review_pk)
    # comment_id = request.POST.get('comment_id')
    # target_comment = Comment.objects.get(pk=comment_id)
    # if request.user == target_comment.user:
    #     target_comment.delete()
    #     target_comment.save()
    #     comment_count = Comment.objects.filter(review=review_pk).exclude(delete()).count()
    #     review.comments = comment_count
    #     review.save()
    #     data = {
    #         'comment_id' : comment_id,
    #         'comment_count' : comment_count,
    #     }
    #     return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")
