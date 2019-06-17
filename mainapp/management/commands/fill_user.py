from django.core.management.base import BaseCommand
from authapp.models import ShopUser



class Command(BaseCommand):
    def handle(self, *args, **options):
       # Создаем суперпользователя при помощи менеджера модели
       user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)
       user.save()

