from django.urls import path

from . import views

app_name = 'production'
urlpatterns = [
    #ex:production/
    path("", views.index, name="index"),
    #ex:production/GMTC-5MM-EFL6.0-AL/stock
    #path("<int:Product_id>/stock/", views.stock, name = "stock"),
    path("<str:Product_pNames>/stock/", views.stock, name = "stock"),
    path("CreateAttribute/", views.CreateAttribute, name = "CreateAttribute"),
    #path("<int:Product_id>/stock/CreateAttribute/", views.CreateAttribute, name = "CreateAttribute"),
    path("createproduct/", views.createproduct, name = "createproduct"),
]
