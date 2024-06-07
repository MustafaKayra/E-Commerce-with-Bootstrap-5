from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.products,name="products"),
    path('categorytelevision/',views.categorytelevision,name="categorytelevision"),
    path('categoryphone/',views.categoryphone,name="categoryphone"),
    path('categorylaptop/',views.categorylaptop,name="categorylaptop"),
    path('categorybluetooth/',views.categorybluetooth,name="categorybluetooth")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)