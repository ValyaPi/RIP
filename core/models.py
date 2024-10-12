from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver



class AnimalAd(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

    KIND_CHOICES = [
        ('Dog', 'Собака'),
        ('Cat', 'Кот'),
        ('Bird', 'Птица')
    ]

    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    kind = models.CharField(max_length=100, choices=KIND_CHOICES, verbose_name='Вид животного')
    breed = models.CharField(max_length=100,  verbose_name='Порода животного')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    location = models.CharField(max_length=255, verbose_name='Местоположение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='animal_images/', verbose_name='Картинка', blank=True, null=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Объявление о животном'
        verbose_name_plural = 'Объявления о животных'


@receiver(post_delete, sender=AnimalAd)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Удаляет файл из файловой системы при удалении записи модели.
    """
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)