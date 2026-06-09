from rest_framework import serializers
from .models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store_item
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['item_image'] = instance.item_image.url if instance.item_image else None
    #     return representation