from django.shortcuts import render
from django.http import HttpResponse
from .models import Book_Item, Book_List


# Create your views here.
def home(response):
    bl = Book_List.objects.get(id=1)
    return render(response, 'main/home.html', {"bl":bl})


def cart(response):
    bl = Book_List.objects.get(id=1)
    return render(response, 'main/cart.html', {"bl":bl})

def addedtocart(response):
    bl = Book_List.objects.get(id=1)
    bi = Book_Item.objects.all()
    for item in bi:
        
        if response.POST.get('c'+str(item.id))=="clicked":
            print(item.id)
            item.cart_boolean = True
            print(item.cart_boolean)
            item.save()
            
    return render(response, 'main/home.html', {"bl":bl})