from django.shortcuts import render

def homepage(request):
    return render(request, 'game_sales.html')