from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Stock, Order
from .serializers import StockSerializer, OrderSerializer

class OrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PortfolioView(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        orders = Order.objects.all()
        portfolio_value = 0
        for order in orders:
            portfolio_value += order.quantity * order.price
        return Response({'portfolio_value': portfolio_value})

class StockView(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        stock_id = kwargs.get('pk')
        stock = get_object_or_404(Stock, pk=stock_id)
        orders = Order.objects.filter(stock=stock)
        stock_value = 0
        for order in orders:
            stock_value += order.quantity * order.price
        return Response({'stock_id': stock_id, 'stock_value': stock_value})