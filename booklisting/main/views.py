from django.shortcuts import render
from django.http import HttpResponse
from .models import Book_Item, Book_List
from django.views.generic import ListView
import json

# Create your views here.

class InfoListView(ListView):
    model = Book_Item
    template_name = 'main/search.html'

    def get_context_data(self, **kwargs):
        context = super(InfoListView, self).get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Book_Item.objects.values()))
        return context
    #
    # def get(self, request, *args, **kwargs):
    #     apple = InfoListView().get_context_data()
    #
    #     return render(request, "main/search.html", context=apple)


def home(response):
    bl = Book_List.objects.get(id=1)
    bi = Book_Item.objects.all()
    for item in bi:

        if response.POST.get('c' + str(item.id)) == "clicked":
            item.cart_boolean = True
            item.count = 1
            item.save()

        if response.POST.get('m' + str(item.id)) == 'minus':
            if item.count > 1:
                item.count -= 1
                item.save()
            elif item.count == 1:
                item.cart_boolean = False
                item.save()

        elif response.POST.get('p' + str(item.id)) == 'plus':
            item.count += 1
            item.save()

    return render(response, 'main/home.html', {"bl":bl})


def cart(response):
    bl = Book_List.objects.get(id=1)
    return render(response, 'main/cart.html', {"bl":bl})


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

