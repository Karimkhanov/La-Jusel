from rest_framework import serializers

from .models import Menu, MenuItem


class MenuSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)


class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    image = serializers.CharField()
    recipe = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return MenuItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.image = validated_data.get('image')
        instance.price = validated_data.get('price')
        instance.recipe = validated_data.get('recipe')
        instance.save()
        return instance


