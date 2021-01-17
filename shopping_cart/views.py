from rest_framework import generics
from rest_framework.views import APIView
from .serializers import CartItemSerializer
from .models import CartItem
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from shop.models import Product


RESPONSES = {
    'true': Response({'success': True}),
    'false': Response({'success': False})
}

class CartItemCreateView(APIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        request.data._mutable = True
        request.data['user'] = request.user.pk
        try:
            model_is_created = self.queryset.filter(order_item=request.data['order_item']).first()
        except:
            return RESPONSES['false']
        if model_is_created:
            try:
                model_is_created.quantity = request.data['quantity']
                model_is_created.save()
                return RESPONSES['true']
            except:
                return RESPONSES['false']
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteItemFromCart(APIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        item = self.queryset.filter(user=request.user, order_item=request.data['order_item']).first()
        if item is None:
            return RESPONSES['false']
        item.delete()
        return RESPONSES['true']

class ClearCart(APIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        item = self.queryset.filter(user=request.user)
        if item is None:
            return RESPONSES['false']
        item.delete()
        return RESPONSES['true']
