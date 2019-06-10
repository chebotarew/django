from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html', {'title': 'Main page'})

def contact(request):
    return render(request, 'mainapp/contact.html', {'title': 'Contact page'})

def about(request):
    return render(request, 'mainapp/about.html', {'title': 'About page'})
