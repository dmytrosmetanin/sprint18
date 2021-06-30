from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class Order_by_UserIDSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.PrimaryKeyRelatedField(read_only= True, source='user.first_name')

    class Meta:
        model = Order
        fields = ('book', 'created_at', 'first_name')
