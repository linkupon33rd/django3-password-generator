import random
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase') == 'on':
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers') == 'on':
        characters.extend(list('0123456789'))
    if request.GET.get('special') == 'on':
        characters.extend(list(r"@%+/!'\#!$^?:,(){}[]~-_."))

    length = int(request.GET.get('length', 14))

    the_password = ''

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})
