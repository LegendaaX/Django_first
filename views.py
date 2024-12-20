from django.shortcuts import render
from datetime import datetime

def index_page(request):
    context = {
        "name": "Ярослав",
        "pages_count": 3
    }
    return render(request, "index.html", context)

def time_page(request):
    now=datetime.now()
    context = {
        "data": now.strftime("%d-%m-%Y"),
        "time":  now.strftime('%H:%M:%S %p')
    }
    return render(request, "time.html", context)

def calc_page (request):
    a = int(request. GET.get('a', 0))
    b = int(request. GET. get('b', 0))
    context = {
    "titLe":'Курс "Промышленное программирование"',
    "a": a,
    "b":b,
    "sum": a + b
    }
    return render(request, "calc.html", context)
