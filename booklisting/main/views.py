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

# def addedtocart(response):
#     # bl = Book_List.objects.get(id=1)
#     # item = bl.book_item_set.get(id=val)
#     return HttpResponse("Hello")