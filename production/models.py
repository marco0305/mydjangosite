from django.db import models

import datetime
# Create your models here.

class Product(models.Model): #建立產品列表
    #設定產品類別
    types = (("Plastic Lens", "塑膠鏡片"), ("機構", "機構"), ("Others", "其它"))
    #設定資料類型
    pNames = models.CharField(max_length=50, unique=True)
    pTypes = models.CharField(max_length=50, choices=types)
    pCaves = models.CharField(max_length=50)
    pModels = models.CharField(max_length=50, unique=True)
    create_time = models.DateTimeField("Create_Time:", auto_now=True)
    
    def __str__(self):
        return self.pNames


class ProductAttribute(models.Model): 
    #設定產品屬性，有很多變形可以設置。
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attCaves = models.CharField(max_length = 5)
    pNotes = models.CharField(max_length = 200)
    attID = models.CharField(max_length=30, unique=True, blank = False, null= True)
    create_time = models.DateTimeField("Create_Time:", auto_now=True)

    def __str__(self):
        return str(self.product.pNames) + "(" + str(self.attCaves) + ")"

class ProductStocks(models.Model):
    #設定庫存
    #stockNumber = models.IntegerField(unique=True)
    stockNumber = models.CharField(max_length=50, unique=True)
    stockitem = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    create_time = models.DateTimeField("Create_Time:", auto_now=False, auto_now_add=True)
    psNumbers = models.IntegerField()
    psNotes = models.CharField(max_length = 200)
    psChecked = models.BooleanField(default=False, help_text='是否檢驗', blank=True, null=True)
    psCheckedDate = models.DateTimeField("Check_Time:", auto_now=False, auto_now_add=False, blank=True, null = True)
    psShipped = models.BooleanField(default=False, help_text='是否出貨', blank=True, null=True)
    psShippedDate = models.DateTimeField("Check_Time:", auto_now=False, auto_now_add=False, blank=True, null = True)
    #barCodeImg = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=None, blank=True)

    def __str__(self):
        return self.stockitem.attID
    
class injection_mold_output(models.Model):
    imo_date = models.DateField()
    line = (("#1","GR-M02-11-1"), ("#2","GR-M02-11-2"), ("#3","GR-M02-11-3"))
    imo_line = models.CharField(max_length= 10, choices = line)
    imo_date = models.DateTimeField(auto_now=False, auto_now_add=False)    
    imo_quantity = models.IntegerField()
    #imo_responsor = 
