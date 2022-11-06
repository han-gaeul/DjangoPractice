from django.shortcuts import render

# Create your views here.

# 글 목록
def index(request):
    return render(request, 'information/index.html')