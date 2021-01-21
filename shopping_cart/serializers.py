from rest_framework import serializers
from .models import CartItem, Product
from shop.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'has_discount', 'cost', 'discount_cost', 'quantity', 'currency', )

class CartListSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField(read_only=True, source='get_product')
    class Meta:
        model = CartItem
        fields = ('quantity', 'product')

    def get_product(self, obj):
        queryset = Product.objects.filter(pk=obj.order_item.pk).first()
        return ProductSerializer(queryset).data
