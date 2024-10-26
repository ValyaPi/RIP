from rest_framework import serializers
from .models import AnimalAd

class AnimalAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalAd
        fields = ['id', 'title', 'description', 'kind', 'breed', 'age', 'gender', 'location', 'price', 'image']