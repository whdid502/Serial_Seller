from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'game_sales.html')
    # return HttpResponse("Hello, world. You're at the polls index.")
