from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return HttpResponse('Olá Mundo.')

def postParams(request, post_id):
    return HttpResponse('Olá mundo %s' %post_id)

def postList(request):
    name = 'Magno Matos'
    return render(request, 'postList.html', {'name': name})