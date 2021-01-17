from rest_framework import serializers
from .models import Category, Product, Image, ProductSize, Order, OrderItem, Sizes


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'

class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ('size', )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'category_name', )

class ProductDetailsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True, source='get_images')
    sizes = serializers.SerializerMethodField(read_only=True, source='get_sizes')
    real_cost = serializers.SerializerMethodField(read_only=True, source='get_real_cost')
    class Meta:
        model = Product
        fields = '__all__'
    
    def get_sizes(self, obj):
        if Category.objects.filter(name=obj.category).first().has_dimensions:
            product_sizes = Sizes.objects.all()[1::]
            return SizesSerializer(product_sizes, many=True, read_only=True).data
    def get_images(self, obj):
        return Image.objects.filter(product=obj).values('pk', 'image')
        return None
    def get_real_cost(self, obj):
        if obj.has_discount:
            return round((obj.cost - (obj.cost * (obj.discount_cost/100))), 2)
        return None
    def get_real_cost(self, obj):
        if obj.has_discount:
            return round((obj.cost - (obj.cost * (obj.discount_cost/100))), 2)
        return None

class ProductSerializer(serializers.ModelSerializer):
    real_cost = serializers.SerializerMethodField(read_only=True, source='get_real_cost')
    image = serializers.SerializerMethodField(read_only=True, source='get_image')
    class Meta:
        model = Product
        fields = ('id', 'name', 'has_discount', 'cost', 'discount_cost', 'image', 'real_cost', 'currency', )

    def get_image(self, obj):
        return Image.objects.filter(product=obj).first().image.url
    def get_real_cost(self, obj):
        if obj.has_discount:
            return round((obj.cost - (obj.cost * (obj.discount_cost/100))), 2)
        return None

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'
    def create(self, validated_data):
        orders_data = validated_data.pop('order_item')
        order = Order.objects.create(**validated_data)
        for order_data in orders_data:
            OrderItem.objects.create(order=order, **order_data)
        return order