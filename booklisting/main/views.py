from django.shortcuts import render
from django.http import HttpResponse
from .models import Book_Item, Book_List
from django.views.generic import ListView
import json

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
            item.cart_boolean = True
            item.count = 1
            item.save()

        if response.POST.get('m' + str(item.id)) == 'minus':
            if item.count > 1:
                item.count -=1
                item.save()
            elif item.count == 1:
                item.cart_boolean = False
                item.save()

        elif response.POST.get('p' + str(item.id)) == 'plus':
            item.count +=1
            item.save()

    return render(response, 'main/home.html', {"bl":bl})   

def cart_update(response):
    bl = Book_List.objects.get(id=1)
    bi = Book_Item.objects.all()
    for item in bi:
        
        if response.POST.get('m' + str(item.id)) == 'minus':
            if item.count > 1:
                item.count -=1
                item.save()
            elif item.count == 1:
                item.cart_boolean = False
                item.save()

        elif response.POST.get('p' + str(item.id)) == 'plus':
            item.count +=1
            item.save()
        
    return render(response, 'main/cart.html', {"bl":bl})

#
# def searchposts(response):

    # b1 = Book_List.objects.get(id=1)
    # b2 = b1.book_item_set.all()
    # c = list(b2.values_list())
    # d = []
    # for items in range(len(c)):
    #     d.append(c[items][2].lower())
    # return render(response, 'main/home.html',{'d':d})

class InfoListView(ListView):
    model = Book_Item
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Book_Item.objects.values()))
        return context

