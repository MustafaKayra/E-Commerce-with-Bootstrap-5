<<<<<<< HEAD
from django.contrib import admin
from django.urls import path,include
from product import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include("product.urls")),
    path('',views.index,name = "index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.contrib import admin
from django.urls import path
from product import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = "index")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 814535c (Add files via upload)
