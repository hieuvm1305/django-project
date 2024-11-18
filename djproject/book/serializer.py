from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        # fields = ['uid', 'title', 'authors', 'category', 'price', 'quantity', 'updated']
        # exclude = ['category']
