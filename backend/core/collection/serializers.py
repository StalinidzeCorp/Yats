from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Collection

User = get_user_model()


class UserCollectionSerializer(UserCreateSerializer):
    class Meta:
        model = Collection
        fields = ('id','name')

from rest_framework import serializers
from .models import CollectionItem

class CollectionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionItem
        fields = '__all__'

class CollectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
