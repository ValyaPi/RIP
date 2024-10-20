from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from core.models import AnimalAd
from django.http import JsonResponse
from .serializers import AnimalAdSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Chat

class AdManipulator(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        ads = AnimalAd.objects.all().values('id','title', 'description', 'kind', 'breed', 'age', 'gender', 'location', 'price', 'image')
        ads_list = list(ads)
        return JsonResponse(ads_list, safe=False)
    
    def post(self, request):
        serializer = AnimalAdSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    def patch(self, request):
        ad_id = request.data.get("id")
        if not ad_id:
            return JsonResponse({"error":"Can not find id"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            animal_ad = AnimalAd.objects.get(pk=ad_id)
        except AnimalAd.DoesNotExist:
            return JsonResponse({'error': 'Can not find ad'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AnimalAdSerializer(animal_ad, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        ad_id = request.data.get("id")
        if not ad_id:
            return JsonResponse({"error":"Can not find id"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            animal_ad = AnimalAd.objects.get(pk=ad_id)
        except AnimalAd.DoesNotExist:
            return JsonResponse({'error': 'Can not find ad'}, status=status.HTTP_404_NOT_FOUND)
        
        animal_ad.delete()

        return JsonResponse({"message":"Ad deleted)"}, status=status.HTTP_200_OK)

class SupportChat(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Получаем текущего пользователя
        user = request.user

        return JsonResponse({'room_name': user.id})


class ChatsListView(APIView):
    permission_classes = [IsAdminUser]  # Доступ только для staff

    def get(self, request):
        # Получаем все чаты
        chats = Chat.objects.all()

        # Сортируем чаты: сначала непрочитанные, затем прочитанные
        sorted_chats = sorted(chats, key=lambda x: x.support_read)

        # Формируем ответ в виде списка словарей
        chats_list = []
            
        for chat in sorted_chats:
            chats_list.append({
                'chat_name': chat.chat_name,
                'support_read': chat.support_read
            })
        

        return JsonResponse({"chats": chats_list})