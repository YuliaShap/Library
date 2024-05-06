from rest_framework import serializers
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'book', 'user', 'created_at', 'end_at', 'plated_end_at']

