from rest_framework import generics
from rest_framework.views import APIView
from .models import Category, Product, Order, OrderItem, ProductSize, Sizes, Image
from .serializers import CategorySerializer, ProductSerializer, ProductDetailsSerializer, OrderSerializer, ImageSerializer, SizesSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from rest_framework.permissions import AllowAny
from rest_framework import serializers


class ImageView(APIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (AllowAny, )

    def get(self, request, filename):
        try:
            with open('images/'+filename, 'rb') as file:
                return HttpResponse(file, content_type="image/jpg")
        except:
            return Response({'message': 'bad image'})

class Categories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Products(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, category):
        category_key = Category.objects.filter(category_name=category).first()
        products = Product.objects.filter(category=category_key)
        products_serializer = ProductSerializer(products, many=True)
        return Response({"name": category_key.name, "data": products_serializer.data})

class NewProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        products = Product.objects.all()[::-1][:6]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductsDetails(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, product_id):
        product = Product.objects.filter(pk=product_id).first()
        serializer_product = ProductDetailsSerializer(product).data
        # sizes = Sizes.objects.all()
        # serializer_sizes = SizesSerializer(sizes, many=True).data
        # serializer_product['sizes'] = serializer_sizes
        return Response(serializer_product)

class MakeOrder(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        unique_id = get_random_string(length=48)
        order_data = request.data
        order_data['order_id'] = unique_id
        order_cost = 0
        for item in order_data['order_item']:
            product = Product.objects.filter(pk=item['product']).first()
            if item['quantity'] > 10 or item['quantity'] > product.quantity or item['quantity'] < 1:
                return Response({'error': 'too many items'})
            cost = product.cost * item['quantity']
            if product.has_discount:
                cost = (product.cost - (product.cost * (product.discount_cost/100))) * item['quantity']
            item['cost'] = cost
            order_cost += cost
            item['size'] = ProductSize.objects.filter(size=Sizes.objects.filter(size=item['size']).first().pk, product=item['product']).first().pk
        order_data['cost'] = order_cost
        # order_data['closed'] = False
        serializer_order = OrderSerializer(data=order_data)
        if serializer_order.is_valid():
            serializer_order.save()
            return Response(serializer_order.data)
        return Response(serializer_order.errors)