# Generated by Django 5.1.1 on 2024-10-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalad',
            name='kind',
            field=models.CharField(choices=[('Dog', 'Собака'), ('Cat', 'Кот'), ('Bird', 'Птица')], max_length=100, verbose_name='Вид животного'),
        ),
    ]
