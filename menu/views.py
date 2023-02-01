from django.shortcuts import render
from django.views.generic import TemplateView

from menu.models import Category, Menu


def base(request):
    return render(request, 'menu/home.html')


def category_page(request, data):
    obj = Menu.objects.get(url=data)
    print(obj)
    return render(request, 'menu/category.html', context={
        "obj": obj
    })