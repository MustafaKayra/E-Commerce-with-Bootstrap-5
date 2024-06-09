<<<<<<< HEAD
from django import forms
from .models import Report

class ReportForm(forms.ModelForm): #Hakkımızda sayfasındaki geri bildirim formu
    class Meta:
        model = Report #Formun model ile bağlantısının yapılması
        fields = ["name","email","report"] #Geri bildirim formunun alanlarının belirtilmesi
=======
from django import forms
from .models import Product

class ProductForm(forms.Modelform):
    class Meta:
        model = Product
        fields = ['name','category']
>>>>>>> 814535c (Add files via upload)
