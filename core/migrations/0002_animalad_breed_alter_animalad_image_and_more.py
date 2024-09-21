# Generated by Django 5.1.1 on 2024-09-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalad',
            name='breed',
            field=models.CharField(blank=True, choices=[('Dog', 'Собака'), ('Cat', 'Кот')], max_length=100, null=True, verbose_name='Порода животного'),
        ),
        migrations.AlterField(
            model_name='animalad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='animal_images/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='animalad',
            name='kind',
            field=models.CharField(max_length=100, verbose_name='Вид животного'),
        ),
    ]
