from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
#def home(request):
#    return HttpResponse('hello there friend!')

#def eggs(request):
#    return HttpResponse('Eggs are so tasty')

def home (request):
    return render(request,'generator/home.html',{'password':'blablabla'})

def password (request):
    
    characters= list('abcdefghijklmnopqrstuvxywz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYWZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%¨&*()+_-'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    lenght=int(request.GET.get('lenght','12')) #default value is 12 - good to have
    thepassword=''

    for x in range(lenght):
        thepassword+=random.choice(characters)

    return render(request, 'generator/password.html',{'password':thepassword})


def about (request):
    return render(request,'generator/about.html')