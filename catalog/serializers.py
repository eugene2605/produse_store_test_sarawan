from rest_framework import serializers

from catalog.models import Category, Product, Cart


class CategorySerializer(serializers.ModelSerializer):
    list_subcategory = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_list_subcategory(self, category):
        return [subcategory.name for subcategory in Category.objects.get(pk=category.pk).subcategory.all()]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    list_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'category', 'subcategory', 'price', 'list_image')

    def get_category(self, product):
        return Product.objects.get(pk=product.pk).subcategory.category.name

    def get_list_image(self, product):
        return [
            Product.objects.get(pk=product.pk).image1.name,
            Product.objects.get(pk=product.pk).image2.name,
            Product.objects.get(pk=product.pk).image3.name,
        ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('quantity',)


class CartListSerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('product', 'quantity', 'total_quantity', 'total_price')

    def get_total_quantity(self, cart):
        if Cart.objects.filter(owner=cart.owner):
            return sum(cart.quantity for cart in Cart.objects.filter(owner=cart.owner))
        return 0

    def get_total_price(self, cart):
        return sum(cart.product.price * cart.quantity for cart in Cart.objects.filter(owner=cart.owner))
