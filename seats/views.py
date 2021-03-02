from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render


def menu(request):
    food = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
    return render(request, 'menu.html', locals())


def math(request, a, b):
    a = float(a)
    b = float(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    t = get_template('math.html')
    c = {'s': s, 'd': d, 'p': p, 'q': q}
    return HttpResponse(t.render(c))
