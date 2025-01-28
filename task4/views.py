from django.shortcuts import render


def index_platform(request):
    pagename = 'Главная страница'
    content = ''
    context = {
        'pagename': pagename,
        'content': content,
    }
    return render(request, 'fourth_task/platform.html', context)


def index_games(request):
    pagename = 'Игры'
    content = ['Mortal Kombat', 'Tekken', 'Street Fighter']
    context = {
        'pagename': pagename,
        'content': content,
    }
    return render(request, 'fourth_task/games.html', context)


def index_cart(request):
    pagename = 'Корзина'
    content = 'Извините, но ваша корзина пуста'
    context = {
        'pagename': pagename,
        'content': content,
    }
    return render(request, 'fourth_task/cart.html', context)
