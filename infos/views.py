from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    c = {'contact': 'Contact', 'bio': 'bio', 'active_page': 'home'}
    return HttpResponse(render(
        request=request,
        template_name='mainpage/main.html',
        context=c
    ))
def bio(request):
    c= {'info1': 'Mam na imie Bartosz',
        'info2': 'Programuje w Python',
        'info3': 'Mieszkam w malym miescie',
        'info4': "Mam 6'2 wysokosci",
        'info5': "Jestem blondynem (takim ciemniejszym)",
        'active_page': 'bio'
        }
    return HttpResponse(render(
        request=request,
        template_name='biopage/bio.html',
        context=c
    ))

def contact(request):
    c = {'active_page': 'contact'}
    return HttpResponse(render(
        request=request,
        template_name='contactpage/contact.html',
        context=c
    ))