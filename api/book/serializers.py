from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        instance = super(BookSerializer, self).create(validated_data)
        instance.save()
        return instance
