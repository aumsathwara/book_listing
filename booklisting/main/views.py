from django.shortcuts import render, redirect
from .models import Book_Item, Book_List
from django.views.generic import ListView
import json
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
a = { }
b = {}
l = []
class InfoListView(ListView):
    model = Book_Item
    template_name = 'main/search.html'

    def get_context_data(self, **kwargs):
        context = super(InfoListView, self).get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Book_Item.objects.values()))
        return context


def clicked(item):
    item.cart_boolean = True
    item.count = 1
    return item.save()

def landingpage(response):
    bl = Book_List.objects.get(id=1)
    return render(response, 'main/landingpage.html', {"bl":bl})

def home(response):
    bl = Book_List.objects.get(id=1)
    bi = Book_Item.objects.all()
    user = response.user.get_username()
    fname = user
    if user not in a.keys():
        l1 = []
        dic = {}
        for item in bi:
            item.count = 0
            item.cart_boolean = False
            item.save()
            dic[item.id] = item.count
            
            l1.append(dic)
            a[user] = l1[0]

            if response.POST.get('c' + str(item.id)) == "clicked":
                item.cart_boolean = True
                a[user][item.id] = 1
                item.count = a[user][item.id]
                item.save()

            if response.POST.get('m' + str(item.id)) == 'minus':
                if item.count > 1:
                    a[user][item.id] -= 1
                    item.count = a[user][item.id]
                    item.save()
                    # b[item.id] = item.count


                elif item.count == 1:
                    item.cart_boolean = False
                    a[user][item.id] = 0
                    item.save()

                    # b.pop(item.id)

                # a[user] = l


            elif response.POST.get('p' + str(item.id)) == 'plus':
                a[user][item.id] += 1
                item.count = a[user][item.id]
                item.save()
    
    else:
        # for i in len(a[user][0]):
        for item in bi:
            # if user in a.keys():
            # l1 = []
            # a[user] = l1.append({item.id : item.count})
            if response.POST.get('c' + str(item.id)) == "clicked":

                item.cart_boolean = True
                a[user][item.id] = 1
                item.count = a[user][item.id]
                item.save()
                # l.append(item.id)
                # l.append(item.count)
                # a[user] = l
                # print(a)

                # if item.id not in b.keys():
                #     b[item.id] = item.count

                # else:
                #     pass

                # a[user] = l


            if response.POST.get('m' + str(item.id)) == 'minus':
                if item.count > 1:
                    a[user][item.id] -= 1
                    item.count = a[user][item.id]
                    item.save()
                    # b[item.id] = item.count


                elif item.count == 1:
                    item.cart_boolean = False
                    a[user][item.id] = 0
                    item.save()

                    # b.pop(item.id)

                # a[user] = l


            elif response.POST.get('p' + str(item.id)) == 'plus':
                a[user][item.id] += 1
                item.count = a[user][item.id]
                item.save()
                # b[item.id] = item.count
                # a[user] = l



    print(a)
    return render(response, 'main/home.html', {"bl":bl, 'fname':fname})

# l.append(b)

def cart(response):
    bl = Book_List.objects.get(id=1)
    return render(response, 'main/cart.html', {"bl":bl})


def cart_update(response):
    bl = Book_List.objects.get(id=1)
    bi = Book_Item.objects.all()
    user = response.user.get_username()
    fname = user
    for item in bi:
        
        if response.POST.get('m' + str(item.id)) == 'minus':
            if item.count > 1:
                a[user][item.id] -= 1
                item.count = a[user][item.id]
                item.save()
                # b[item.id] = item.count
            elif item.count == 1:
                item.cart_boolean = False
                a[user][item.id] = 0
                item.save()
                # b.pop(item.id)
            # a[user] = l


        elif response.POST.get('p' + str(item.id)) == 'plus':
            a[user][item.id] += 1
            item.count = a[user][item.id]
            item.save()
            
    print(a)    
    return render(response, 'main/cart.html', {"bl":bl})

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been created.")

        return redirect('signin')

    return render(request, "main/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            bl = Book_List.objects.get(id=1)
            context = {'fname':fname,"bl":bl}
            return render(request, "main/home.html", {'fname':user,"bl":bl})


        else:
            messages.error(request, "Bad credentials")
            return redirect('signin')

    return render(request, "main/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('signin')


#
# {'user':[item_id, item_count]}
# {'heta': [15,2]
#  'aum':[16,1]}
