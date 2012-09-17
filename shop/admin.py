# -*- coding: utf-8 -*-
from django.contrib import admin

from shop import models


class ProductInline(admin.TabularInline):
    model = models.ClientProduct

class ClienAdmin(admin.ModelAdmin):
    inlines = [ProductInline]    


admin.site.register(models.Product)
admin.site.register(models.Client, ClienAdmin)
admin.site.register(models.ClientProduct)
admin.site.register(models.Document)
admin.site.register(models.DocumentProduct)
admin.site.register(models.Sheet)
