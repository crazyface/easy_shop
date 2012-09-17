# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import force_unicode


# Create your models here.
class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [['piece', u'Штучный'],
                            ['weight', u'Весовой'],]
    name = models.CharField(max_length=255,
                            verbose_name=u'Наименование Товара')
    product_type = models.CharField(max_length=255,
                            verbose_name=u'Тип Товара',
                            choices=PRODUCT_TYPE_CHOICES)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Client(models.Model):
    CLIENT_CHOICES = [
                      [u'provider', u'прставщик'],
                      [u'storage', u'склад'],
                      [u'shop', u'магазин'],
                      [u'buyer', u'покупатель'],
                      [u'inventory', u'переучет'],
                      ]
    name = models.CharField(max_length=255,
                            verbose_name=u'Имя Клиента')
    contacts = models.TextField(verbose_name=u'Контакты',
                                null=True, blank=True)
    client_type = models.CharField(max_length=255,
                                   verbose_name=u'Тип Клиента',
                                   choices=CLIENT_CHOICES)

    def __unicode__(self):
        return '%s (%s)' % (self.name, str(self.client_type))


class ClientProduct(models.Model):
    product = models.ForeignKey('Product', verbose_name=u'Продукт')
    client = models.ForeignKey('Client', verbose_name=u'Клиент')
    price_in = models.DecimalField(max_digits=10, decimal_places=2,
                                   verbose_name=u'Цена оптовая')
    price_out = models.DecimalField(max_digits=10, decimal_places=2,
                                    verbose_name=u'Цена розничная')
    quantity = models.DecimalField(max_digits=10, decimal_places=3,
                                    verbose_name=u'Колличество')

    def __unicode__(self):
        return '%s (%s)' % (self.product.name, self.quantity)


class Document(models.Model):
    DOC_TYPE_CHOICES = [['delivery', u'Поставка'],
                        ['sale', u'Продажа']]

    user = models.ForeignKey('auth.User', verbose_name=u'Оператор')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=u'Дата создания')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name=u'Дата изменения')
    sender = models.ForeignKey('Client', verbose_name=u'Отправитель',
                               related_name='sent')
    recipient = models.ForeignKey('Client', verbose_name=u'Получатель',
                               related_name='received')
    type = models.CharField(max_length=255, verbose_name='Тип Документа',
                            choices=DOC_TYPE_CHOICES)
    
    deleted = models.BooleanField(default=False)


class DocumentProduct(models.Model):
    product = models.ForeignKey('Product', verbose_name=u'Продукт')
    document = models.ForeignKey('Document', verbose_name=u'Документ')
    price_in = models.DecimalField(max_digits=10, decimal_places=2,
                                   verbose_name=u'Цена оптовая')
    price_out = models.DecimalField(max_digits=10, decimal_places=2,
                                    verbose_name=u'Цена розничная')
    quantity = models.DecimalField(max_digits=10, decimal_places=3,
                                    verbose_name=u'Колличество')


class Sheet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=u'Дата создания')
    sales = models.ManyToManyField('Document', verbose_name=u'Продажи') 