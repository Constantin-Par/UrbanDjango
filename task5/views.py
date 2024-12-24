from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegistrationForm


def sign_up_by_html(request):
    users = [
            'Nick',
            'Jack',
            'Petr',
            'Igor',
            ]

    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        info = {}

        if username in users:
            info = {'error': f"Пользователь '{username}' уже существует"}
        elif password != repeat_password:
            info = {'error': 'Пароли не совпадают'}
        elif age < 18:
            info = {'error': 'Вы должны быть старше 18 лет'}
        else:
            return HttpResponse(f'Приветствуем, {username}')

        return render(request, 'registration_page.html', {'info': info})

    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    users = [
            'Nick',
            'Jack',
            'Petr',
            'Igor',
            ]

    info = {}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username'].strip()
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info = {'error': f"Пользователь '{username}' уже существует"}
            elif password != repeat_password:
                info = {'error': 'Пароли не совпадают'}
            elif age < 18:
                info = {'error': 'Вы должны быть старше 18 лет'}

            if not info:
                return HttpResponse(f'Приветствуем, {username}')

    else:
        form = RegistrationForm()

    return render(request, 'registration_page.html', {'form': form, 'info': info})
