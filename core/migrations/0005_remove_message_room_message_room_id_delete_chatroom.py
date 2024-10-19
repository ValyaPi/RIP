# Generated by Django 5.1.1 on 2024-10-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_chatroom_name_alter_chatroom_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.AddField(
            model_name='message',
            name='room_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
    ]
