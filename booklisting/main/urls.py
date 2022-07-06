from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    # path("addedtocart", views.addedtocart, name="addedtocart"),
    path("cart/cart_update", views.cart_update, name="cart_update"),
    path("search/",views.InfoListView.as_view(), name="search"),
    path('', views.index, name ='index'),
]
