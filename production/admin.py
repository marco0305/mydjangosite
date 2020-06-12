<<<<<<< HEAD
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
=======
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
>>>>>>> 56afbab79133fcfce23ab4f0188ae22f935e9d9d
admin.site.register(ProductStocks, ProductStocksAdmin)