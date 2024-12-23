from django.shortcuts import render
from django.views.generic import TemplateView


def task4_platform(request):
    context = {
            'pagename': 'Главная страница',
            }
    return render(request, 'platform.html', context)


def task4_games(request):
    context = {
            'pagename':   'Игры',
            'games_list': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2', 'Warcraft III: Reforged'],
            }
    return render(request, 'games.html', context)


def task4_cart(request):
    context = {
            'pagename': 'Корзина',
            }
    return render(request, 'cart.html', context)
