from django.core.management.base import BaseCommand
from mainapp.models import Page



class Command(BaseCommand):
    def handle(self, *args, **options):
       # Создаем суперпользователя при помощи менеджера модели
       main_page = Page(name='Main', text='Welcome to main page', image='pages_images/1.jpg')
       main_page.save()

       contact_page = Page(name='Contact', text='Welcome to contact page', image='pages_images/2.jpg')
       contact_page.save()

       about_page = Page(name='About', text='Welcome to about page', image='pages_images/3.gif')
       about_page.save()



