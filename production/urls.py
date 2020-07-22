from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'production'
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:Product_pNames>/stock/", views.stock, name = "stock"),
    path("<str:Product_pNames>/stock/<int:ProductStocks_stockNumber>/", views.stockdetail, name = "stockdetail"),
    path("CreateAttribute/", views.CreateAttribute, name = "CreateAttribute"),
    path("createproduct/", views.createproduct, name = "createproduct"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#https://docs.djangoproject.com/en/3.0/howto/static-files/