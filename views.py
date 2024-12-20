from django.shortcuts import render
import time

def index_page(request):
    context = {
        "name": "Ярослав",
        "pages_count": 2
    }
    return render(request, "index.html", context)

def time_page(request):
    context = {
        "data": time,
        "time":  time.strftime('%H:%M:%S %p')
    }
    return render(request, "time.html", context)