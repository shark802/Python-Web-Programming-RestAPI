from rest_framework import serializers
from .models import Stock, Order

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name', 'price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['stock', 'quantity', 'price', 'created_at']