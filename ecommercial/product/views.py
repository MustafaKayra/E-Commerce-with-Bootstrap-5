from django.shortcuts import render,redirect
from .forms import ReportForm
from django.contrib import messages
from .models import Product

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    form = ReportForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        form.save()
        messages.success(request,"Geri Bildiriminiz Başarıyla İletildi")
        return redirect('contact')

    return render(request,"contact.html",context)

def products(request):
    product = Product.objects.all()
    context = {
        "product":product
    }
    return render(request,"products.html",context)

def categorytelevision(request):
    television = Product.objects.filter(category=1)
    context = {
        "television":television
    }
    return render(request,"categorytelevision.html",context)

def categoryphone(request):
    phone = Product.objects.filter(category=2)
    context={
        "phone":phone
    }
    return render(request,"categoryphone.html",context)

def categorylaptop(request):
    laptop = Product.objects.filter(category=3)
    context = {
        "laptop":laptop
    }
    return render(request,"categorylaptop.html",context)

def categorybluetooth(request):
    bluetooth = Product.objects.filter(category=4)
    context = {
        "bluetooth":bluetooth
    }
    return render(request,"categorybluetooth.html",context)