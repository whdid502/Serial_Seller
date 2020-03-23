from django.shortcuts import render
from django.http import HttpResponse

def sales_page(request):
    return render(request, 'sell_page.html')