from django import forms
from production.models import Product, ProductAttribute
class CreateProductForm(forms.Form):
    #設定產品類別
    types = (("Plastic Lens", "塑膠光學鏡片"), ("Optical Lens", "光學鏡頭"), ("Others", "其它"))
    pNames = forms.CharField(max_length=50, label = "產品名稱")
    pTypes = forms.ChoiceField(choices=types, label = "產品類型")
    pCaves = forms.CharField(max_length=50, label = "產品穴數")
    pModels = forms.CharField(max_length=50, label = "產品型號")

class CreateAttributeForm(forms.Form):
    product = forms.ModelChoiceField(queryset = Product.objects.all())
    attCaves = forms.CharField(max_length = 5)
    pNotes = forms.CharField(max_length = 200)

class CreateSotckForm(forms.Form):
    stockitem = forms.ModelChoiceField(queryset = ProductAttribute.objects.all())
    #create_time = forms.DateTimeField(auto_now=True)
    psNumbers = forms.IntegerField()
    psNotes = forms.CharField(max_length = 200)
    #psChecked = forms.BooleanField(required=False)
    #psCheckedDate = forms.DateTimeField(required=False)
    #psShipped = forms.BooleanField(required=False)
    #psShippedDate = forms.DateTimeField(required=False)