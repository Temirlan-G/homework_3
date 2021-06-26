from django.db import models


# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название', max_length=255, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    title = models.CharField('Название', max_length=255, blank=False)
    description = models.CharField('Описание', max_length=255, null=True, blank=True)
    price = models.IntegerField('Цена', blank=False)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    text = models.CharField('Текст', max_length=255)
    date = models.DateTimeField('Дата', auto_now=True, null=False)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

