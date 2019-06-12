from django.shortcuts import render
from .models import Page


def main(request):
    page = Page.objects.all()[0]
    context = {'page': page}
    return render(request, 'mainapp/index.html', context)

def contact(request):
    page = Page.objects.all()[1]
    context = {'page': page}
    return render(request, 'mainapp/contact.html', context)

def about(request):
    page = Page.objects.all()[2]
    context = {'page': page}
    return render(request, 'mainapp/about.html', context)
