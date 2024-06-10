from rest_framework import generics, request
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Category, Product, Cart
from catalog.paginators import CategoryPaginator, ProductPaginator
from catalog.serializers import CategorySerializer, ProductSerializer, CartSerializer, CartUpdateSerializer, \
    CartListSerializer
from users.permissions import IsOwner


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPaginator
    permission_classes = [AllowAny]


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPaginator
    permission_classes = [AllowAny]


class CartCreateAPIView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_cart = serializer.save(owner=self.request.user)
        new_cart.save()


class CartListAPIView(generics.ListAPIView):
    serializer_class = CartListSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(owner=user)


class CartUpdateAPIView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartUpdateSerializer
    permission_classes = [IsOwner]


class CartDestroyAPIView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    permission_classes = [IsOwner]


class CartAllDeleteAPIView(APIView):

    def get(self, request):
        user = self.request.user
        Cart.objects.filter(owner=user).delete()
        return Response()
