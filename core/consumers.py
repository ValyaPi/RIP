import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message, Chat

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        # Получаем текущего пользователя
        user = self.scope['user']
        
        # Проверяем, что пользователь авторизован
        if user.is_anonymous:
            await self.close()
            return

        self.room_name = self.scope['url_route']['kwargs']['room_name']

        # Создаем чат, если он не существует
        self.chat = await self.get_or_create_chat(self.room_name)

        # Если у пользователя статус Staff, он может подключаться ко всем чатам
        if user.is_staff:
            # Присоединяем к группе чата
            self.room_group_name = f'chat_{self.room_name}'
        else:
            # Проверка, что пользователь подключается к своей комнате
            if self.room_name != str(user.id):
                await self.close()
                return
            
            self.room_group_name = f'chat_{self.room_name}'

        # Присоединяем пользователя к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Отправляем историю сообщений
        messages = await self.get_messages()
        for message in messages:
            print("Отправка")
            await self.send(text_data=json.dumps({
                'type': 'chat_message',
                'message': message.content
            }))
        
        if user.is_staff:
            print("Техподдержка прочитала")
            await self.update_support_read_status(True)
        
        

    async def receive(self, text_data):
        # Получаем текст сообщения
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Сохраняем сообщение в базе данных
        await self.save_message(message)

        # Сразу после получения считаем чат не прочтенным поддержкой
        await self.update_support_read_status(False)
        print("Техподдержка еще не прочитала")

        # Отправляем сообщение всем участникам группы
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
        print("Да ведь?")
        # Если пользователь со статусом Staff, обновляем статус прочтения
        if self.scope['user'].is_staff:
            print("Техподдержка прочитала")
            await self.update_support_read_status(True)

    @database_sync_to_async
    def update_support_read_status(self, status):
        # Обновляем поле support_read в объекте Chat
        self.chat.support_read = status
        self.chat.save()

    @database_sync_to_async
    def save_message(self, message_content):
        user = self.scope['user']
        Message.objects.create(user=user, room_id=self.room_name, content=message_content)

    @database_sync_to_async
    def get_messages(self):
        return list(Message.objects.filter(room_id=self.room_name).order_by('-timestamp').all())
    
    @database_sync_to_async
    def get_or_create_chat(self, room_id):
        chat, created = Chat.objects.get_or_create(
            chat_name=room_id,
            defaults={'support_read': False}  # Устанавливаем значение по умолчанию
        )
        return chat