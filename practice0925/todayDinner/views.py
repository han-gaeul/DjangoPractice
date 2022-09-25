import random
from django.shortcuts import render

# Create your views here.

def todayDinner(request):
    foodList = [
        {'name' : '삼겹살', 'src' : 'https://src.hidoc.co.kr/image/lib/2021/8/27/1630049987719_0.jpg'},
        {'name' : '족발', 'src' : 'http://image.auction.co.kr/itemimage/23/f5/a6/23f5a6ee96.jpg'},
        {'name' : '치킨', 'src' : 'https://upload.wikimedia.org/wikipedia/commons/2/20/Korean_fried_chicken_3_banban.jpg'},
        {'name' : '아구찜', 'src' : 'https://recipe1.ezmember.co.kr/cache/recipe/2021/08/05/98998b80a8bba88b91b8829417f416a61.jpg'},
        {'name' : '수육', 'src' : 'https://recipe1.ezmember.co.kr/cache/recipe/2016/07/15/e9d94fdf4f545ed3cb9ff30748bf88e71.jpg'},
    ]
    food = random.choice(foodList)
    context = {
        'food' : food
    }
    return render(request, 'todayDinner.html', context)