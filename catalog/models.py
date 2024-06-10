from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    image = models.ImageField(upload_to='catalog/category', verbose_name='изображение')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Subcategory(models.Model):
    name = models.CharField(max_length=70, verbose_name='наименование')
    slug = models.SlugField(max_length=70, db_index=True, unique=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория',
                                 related_name='subcategory')
    image = models.ImageField(upload_to='catalog/subcategory', verbose_name='изображение')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.PROTECT, verbose_name='подкатегория')
    image1 = models.ImageField(upload_to='catalog/product', verbose_name='изображение1')
    image2 = models.ImageField(upload_to='catalog/product', verbose_name='изображение2')
    image3 = models.ImageField(upload_to='catalog/product', verbose_name='изображение3')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='цена')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Cart(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, verbose_name='владелец')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.SmallIntegerField(verbose_name='количество')

    def __str__(self):
        return f'Корзина пользователя {self.owner}'

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
        ordering = ('owner',)
