from django.contrib import admin
from django.urls import path
from singhdarbarapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('sweets-dhaba', views.sweetsDhaba, name='sweetsDhaba'),
    path('pan-india', views.panIndia, name='panIndia'),
    path('contact', views.contact, name='contact'),
    path('product-detail/<str:slug>/', views.productDetail, name='product-detail'),
]