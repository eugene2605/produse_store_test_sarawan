from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListAPIView, ProductListAPIView, CartCreateAPIView, CartUpdateAPIView, \
    CartDestroyAPIView, CartListAPIView, CartAllDeleteAPIView

app_name = CatalogConfig.name


urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('product/', ProductListAPIView.as_view(), name='product-list'),
    path('cart/create/', CartCreateAPIView.as_view(), name='cart-create'),
    path('cart/update/<int:pk>', CartUpdateAPIView.as_view(), name='cart-update'),
    path('cart/destroy/<int:pk>', CartDestroyAPIView.as_view(), name='cart-destroy'),
    path('cart/list/', CartListAPIView.as_view(), name='cart-list'),
    path('cart/alldestroy/', CartAllDeleteAPIView.as_view(), name='cart-alldestroy'),
]
