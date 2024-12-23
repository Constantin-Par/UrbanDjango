from django.shortcuts import render
from django.views.generic import TemplateView


def task3_platform(request):
    context = {
            'title': 'Главная страница',
            'main':  'Главная',
            'games': 'Магазин',
            'cart':  'Корзина'
            }
    return render(request, 'platform.html', context)


def task3_games(request):
    context = {
            'title': 'Магазин',
            'main':  'Игры',
            'game_1':  'Atomic Heart',
            'game_2':  'Cyberpunk 2077',
            'game_3':  'PayDay2',
            }
    return render(request, 'games.html', context)


def task3_cart(request):
    context = {
            'title': 'Магазин',
            'main':  'Корзина',
            }
    return render(request, 'cart.html', context)
