from rest_framework import serializers
from .models import Interactor

class InteractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interactor
        fields = ('pos', 'money','propertyBought', 'propertyExpanded','housesBought')
