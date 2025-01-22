from django.shortcuts import render


# Create your views here.
def index_platform(request):
    title = 'Главная страница'
    text1 = 'Главная'
    text2 = 'Магазин'
    text3 = 'Корзина'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3,
    }
    return render(request, 'third_task/platform.html', context)


def index_games(request):
    title = 'Игры'
    text1 = 'Mortal Kombat'
    text2 = 'Tekken'
    text3 = 'Street Fighter'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3,
    }
    return render(request, 'third_task/games.html', context)


def index_cart(request):
    title = 'Корзина'
    text = 'Извините, но ваша корзина пуста'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'third_task/cart.html', context)
