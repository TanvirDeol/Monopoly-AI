from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import InteractorSerializer
from .models import Interactor
from rest_framework import status
import player

# Create your views here.

class InteractorView(viewsets.ModelViewSet):
    serializer_class = InteractorSerializer
    queryset = Interactor.objects.all()

    def update(self, request, *args, **kwargs):
        print("Works")
        instance = self.get_object()
        data = request.data
        print(instance)
        print(data)
        instance.pos = data['pos']
        instance.money = data['money']
        instance.propertyBought = data['propertyBought']
        instance.propertyExpanded = data['propertyExpanded']
        instance.housesBought = data['housesBought']
        
        instance.save()
        serializer = InteractorSerializer(instance)
        player.play(data['pos'],data['money'],data['propertyBought'],data['propertyExpanded'],data['housesBought'])
        return Response(serializer.data)