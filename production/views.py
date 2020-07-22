from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product, ProductAttribute, ProductStocks
from django.db.models import Sum
import datetime

def index(request):
    products = Product.objects.all()
    ps = [] #用來存查詢整理後的資料，再整體匯出成網頁資料。
    a = 0 #用來取得products的字典資料。

    for x in products:
        try:
            '''
            "__in" can handle querysets larger than one (multiple records of a table).
            This can be found in the django Many-to_one relationships section of the documentation. 
            https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/
            Django documentation can be scary for a beginner like me because of its length and depth, 
            though it provides solutions to most issues if you can crack it.
            '''
            stock = ProductStocks.objects.filter(stockitem__in = ProductAttribute.objects.filter(product_id = x.id)).aggregate(Sum('psNumbers'))
            temp = products.values()[a]
            ps.append(temp)
            a = a + 1
            temp.update(stock)
        except:
            temp = products.values()[a]
            ps.append(temp)
    #return render(request, 'production/index.html', {"products": products})
    return render(request, 'production/index.html', {"ps": ps})


#由網頁輸入到資料庫；
from production.forms import CreateProductForm, CreateAttributeForm, CreateSotckForm

def createproduct(request):
    #create = get_object_or_404(Product)
    if request.method == "POST":
        cpf = CreateProductForm(request.POST)
        if cpf.is_valid():
            Product(
                pNames = cpf.cleaned_data['pNames'],
                pTypes = cpf.cleaned_data['pTypes'],
                pCaves = cpf.cleaned_data['pCaves'],
                pModels = cpf.cleaned_data['pModels'],
                ).save()
            cpf = CreateProductForm()
    else:
        cpf = CreateProductForm()
    return render(request, 'production/createproduct.html', {"cpf": cpf})

def CreateAttribute(request):
    #product = Product.objects.get(pk = Product_id)
    #attribute = ProductAttribute.objects.filter(product = product)
    caf = CreateAttributeForm()
    if request.method == "POST":
        caf = CreateAttributeForm(request.POST)
        if caf.is_valid():
            ProductAttribute(
                product = caf.cleaned_data['product'],
                attCaves = caf.cleaned_data['attCaves'],
                pNotes = caf.cleaned_data['pNotes'],
                attID = str(caf.cleaned_data['product']) + "-" + str(caf.cleaned_data['attCaves'],)
            ).save()
        caf = CreateAttributeForm()

    return render(request, 'production/creatrpatt.html', {"caf": caf})

import barcode
from barcode.writer import ImageWriter

def batCodeSvgGenerator(stockNumber):
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(stockNumber, writer=ImageWriter())
    ean.save("media\\uploads\\" + str(stockNumber))
    return "media\\uploads\\" + str(stockNumber) + ".png"

def stock(request, Product_pNames):
    product = Product.objects.get(pNames = Product_pNames)
    attribute = ProductAttribute.objects.filter(product = product)
    att = []
    b = 0 #常數，只拿來取出數據的而己。
    for a in attribute:
        stock = ProductStocks.objects.filter(stockitem__in = ProductAttribute.objects.filter(pk = a.id)).aggregate(Sum('psNumbers'))
        #TODO: 把#1 #2的庫存總和整理到頁面去。
        temp = attribute.values()[b]
        #ps.append(temp)
        b = b + 1
        temp.update(stock)
        att.append(temp)
    csf = CreateSotckForm()
    

    if request.method == "POST":
        #將是否檢驗的checkbox核對是否勾取，並更新狀態。
        temp = ProductStocks.objects.all()
        a = request.POST
        for t in temp:
            for i in a.keys():
                if ("check" + str(t.id)) == i:
                    t.psChecked = True
                    t.psCheckedDate = datetime.datetime.now()
                    t.save()
                elif ("shipped" + str(t.id)) == i:
                    t.psShipped = True
                    t.psShippedDate = datetime.datetime.now()
                    t.save()


        #------以下是建立庫存表單分隔線
        csf = CreateSotckForm(request.POST)
        
        if csf.is_valid():
            yearmonth = datetime.datetime.now().strftime("%Y%m%d")
            numbers = str(len(ProductStocks.objects.filter(create_time__month = datetime.datetime.now().month, 
            create_time__year = datetime.datetime.now().year))).zfill(2)
            ProductStocks(
                stockNumber = yearmonth + numbers,
                stockitem = csf.cleaned_data['stockitem'],
                psNumbers = csf.cleaned_data['psNumbers'],
                psNotes = csf.cleaned_data['psNotes'],
                #psChecked = csf.cleaned_data['psChecked'],
                #psShipped = csf.cleaned_data['psShipped']
                #barCodeSvg = batCodeSvgGenerator(yearmonth + numbers)
                barCodeImg = batCodeSvgGenerator(yearmonth + numbers)
            ).save()
        csf = CreateSotckForm()
    
    
    if attribute.exists():
        stocks = ProductStocks.objects.filter(stockitem__in = attribute)
        '''
        "__in" can handle querysets larger than one (multiple records of a table).
        This can be found in the django Many-to_one relationships section of the documentation. 
        https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/
        Django documentation can be scary for a beginner like me because of its length and depth, 
        though it provides solutions to most issues if you can crack it.
        '''
        if stocks.exists():
            print("正常運作。")
        else:
            stocks = {}
            print("沒有庫存。")

    return  render(request, 'production/stock.html',{'att':att, 'product':product, "stocks": stocks, "csf": csf})

    #TODO:barcode programing

def stockdetail(request, Product_pNames, ProductStocks_stockNumber):
    pNames = Product_pNames
    stockNumber = ProductStocks_stockNumber
    output = ProductStocks.objects.filter(stockNumber = stockNumber)
    return render(request, 'production/stockdetail.html', {'output': output})
    