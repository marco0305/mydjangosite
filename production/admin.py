from django.contrib import admin

# Register your models here.
from .models import Product, ProductAttribute, ProductStocks

class productAdmin(admin.ModelAdmin):
    list_display = ("id", "pNames", "pTypes", "pCaves", "pModels", "create_time")

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ("product", "attCaves", "pNotes", "create_time", "attID")

class ProductStocksAdmin(admin.ModelAdmin):
    list_display = ("stockitem", "create_time", "psNumbers", "psNotes")

admin.site.register(Product, productAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(ProductStocks, ProductStocksAdmin)