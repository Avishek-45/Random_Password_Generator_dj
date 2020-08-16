from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'home.html',{'Password':'jsdjasjjh'})

def base(request):
    characters=list('abcdefghijkmlnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789')) 
    if request.GET.get('Characters'):
        characters.extend(list('!~`#$%^&*()_+,.<>?:"'))

    length=int(request.GET.get('length'))

    thisispass=''
    for x in range(length):
        thisispass += random.choice(characters)

    return render(request,'password.html',{'word':thisispass})