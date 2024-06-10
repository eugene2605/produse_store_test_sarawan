# Generated by Django 5.0.6 on 2024-06-06 04:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='catalog/category', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image1', models.ImageField(upload_to='catalog/product', verbose_name='изображение1')),
                ('image2', models.ImageField(upload_to='catalog/product', verbose_name='изображение2')),
                ('image3', models.ImageField(upload_to='catalog/product', verbose_name='изображение3')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='цена')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(verbose_name='количество')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'корзина',
                'verbose_name_plural': 'корзины',
                'ordering': ('owner',),
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='наименование')),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('image', models.ImageField(upload_to='catalog/subcategory', verbose_name='изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'подкатегория',
                'verbose_name_plural': 'подкатегории',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.subcategory', verbose_name='подкатегория'),
        ),
    ]
