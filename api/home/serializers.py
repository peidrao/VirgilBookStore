from rest_framework import serializers


class BookHomeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.FloatField()
    image = serializers.ImageField()
