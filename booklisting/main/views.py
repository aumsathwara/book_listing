from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book_Item, Book_List
from django.views.generic import ListView
import json
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import UserRegisterForm

# Create your views here.

class InfoListView(ListView):
    model = Book_Item
    template_name = 'main/search.html'

    def get_context_data(self, **kwargs):
        context = super(InfoListView, self).get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Book_Item.objects.values()))
        return context

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

def index(request):
    return render(request, 'main/index.html', {'title':'index'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('main/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'booklistingtest@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'Your account has been created! You can log in now!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form, 'title':'Register Here'})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'Username or password is incorrect. Please log in with correct credentials or create a new account.')
    form = AuthenticationForm()
    return render(request, 'main/login.html', {'form':form, 'title':'log in'})