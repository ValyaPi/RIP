# Generated by Django 5.1.1 on 2024-09-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('kind', models.CharField(choices=[('Dog', 'Собака'), ('Cat', 'Кот')], max_length=100, verbose_name='Вид животного')),
                ('breed', models.CharField(max_length=100, verbose_name='Порода животного')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, verbose_name='Пол')),
                ('location', models.CharField(max_length=255, verbose_name='Местоположение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='animal_images/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Объявление о животном',
                'verbose_name_plural': 'Объявления о животных',
            },
        ),
    ]
