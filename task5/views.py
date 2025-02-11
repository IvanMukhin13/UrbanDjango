from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


users = ['Superman', 'Batman', 'Wonder Woman', 'Green Lantern', 'The Flash', 'Aquaman', 'Cyborg']


def sign_up_by_django(request):
    info = {'error': []}
    i = 0
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in users and password == repeat_password and int(age) >= 18:
                users.append(username)
                print(users)
                return HttpResponse(f'Приветствуем {username}')
            elif username in users:
                i += 1
                info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
                print(info[f'error {i}'])
                return HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
            elif password != repeat_password:
                i += 1
                info[f'error {i}'] = HttpResponse('Пароли не совпадают', status=400, reason='The passwords do not match')
                print(info[f'error {i}'])
                return HttpResponse('Пароли не совпадают', status=400, reason='The passwords do not match')
            elif int(age) < 18:
                i += 1
                info[f'error {i}'] = HttpResponse(
                    'Вы должны быть старше 18', status=400, reason='insufficient age')
                return HttpResponse('Вы должны быть старше 18', status=400, reason='insufficient age')
    else:
        form = UserRegister()
        context = {'info': info, 'form': form}
        return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_html(request):
    i = 0
    info = {'error': []}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Repeat password: {repeat_password}')
        print(f'Age: {age}')

        if username not in users and password == repeat_password and int(age) >= 18:
            users.append(username)
            print(users)
            return HttpResponse(f'Приветствуем {username}')
        elif username in users:
            i += 1
            info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
            return HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
        elif password != repeat_password:
            i += 1
            info[f'error {i}'] = HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
        elif int(age) < 18:
            i += 1
            info[f'error {i}'] = HttpResponse('Вы должны быть старше 18', status=400, reason='insufficient age')
            return HttpResponse('Вы должны быть старше 18', status=400, reason='insufficient age')
    context = {'info': info}

    return render(request, 'fifth_task/registration_page.html', context)