from django.core.management.base import BaseCommand
from core.models import AnimalAd

class Command(BaseCommand):
    help = 'Выводит список всех объявлений о животных'

    def handle(self, *args, **kwargs):
        ads = AnimalAd.objects.all()
        if not ads.exists():
            self.stdout.write(self.style.WARNING('Нет объявлений о животных.'))
        else:
            for ad in ads:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Название: {ad.title}, Вид: {ad.get_kind_display()}, "
                        f"Порода: {ad.breed}, Возраст: {ad.age} лет, Пол: {ad.get_gender_display()}, "
                        f"Цена: {ad.price}, Местоположение: {ad.location}"
                    )
                )
