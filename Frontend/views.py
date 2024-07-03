from django.shortcuts import render, redirect
from Jioapp.models import ProductDB, CategoryDB
from Frontend.models import ContactDB, RegistrationDB, CartDB, CheckoutDB
from django.contrib import messages

# Create your views here.
def homepage(request):
    pro = ProductDB.objects.all()
    cat = CategoryDB.objects.all()
    return render(request, "home.html", {'pro': pro, 'cat': cat})

def product_page(request, cname):
    pro = ProductDB.objects.filter(CName=cname)
    return render(request, "Products.html", {'pro': pro})

def aboutpage(request):
    cat = CategoryDB.objects.all()
    return render(request, "About.html", {'cat': cat})

def contactpage(request):
    cat = CategoryDB.objects.all()
    return render(request, "Contact.html", {'cat': cat})

def singleproduct(request, proid):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.get(id=proid)
    return render(request, "SingleProduct.html", {'pro': pro, 'cat': cat})

def contactsave(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('sub')
        d = request.POST.get('mes')
        obj = ContactDB(Name=a, Email=b, Subject=c, Message=d)
        obj.save()
        return redirect(contactpage)
#   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

def userlogin(request):
    return render(request, "Userlogin.html")

def reg_save(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('password')
        obj = RegistrationDB(Name=a, Email=b, Password=c)
        obj.save()
        return redirect(userlogin)

def signup_page(request):
    if request.method == "POST":
        nm = request.POST.get('name')
        pwd = request.POST.get('password')
        if RegistrationDB.objects.filter(Name=nm, Password=pwd).exists():
            request.session['Name']=nm
            request.session['Password']=pwd
            return redirect(homepage)
        else:
            return redirect(userlogin)
    else:
        return redirect(userlogin)

def Userlogout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(userlogin)
#   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
def cart_save(request):
    if request.method == "POST":
        a = request.POST.get('uname')
        b = request.POST.get('pname')
        c = request.POST.get('qty')
        d = request.POST.get('price')
        e = request.POST.get('TotalPrice')
        obj = CartDB(UserName=a, Productname=b, Quantity=c, Price=d, TotalPrice=e)
        obj.save()
        messages.success(request, "Added To Cart")
        return redirect(homepage)

def cartpage(request):
    data =CartDB.objects.filter(UserName=request.session['Name'])
    total_price =0
    for i in data:
        total_price = total_price+i.TotalPrice
    cat = CategoryDB.objects.all()
    return render(request, "Cart.html", {'data':data, 'total_price': total_price, 'cat': cat})
def cartdelete(request, p_id):
    cart = CartDB.objects.filter(id=p_id)
    cart.delete()
    messages.error(request, "Delete!")
    return redirect(cartpage)
def checkoutpage(request):
    data = CartDB.objects.filter(UserName=request.session['Name'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    cat = CategoryDB.objects.all()
    return render(request, "Checkout.html",  {'data':data, 'total_price': total_price, 'cat': cat})
def save_checkout(req):
    if req.method == "POST":
        a = req.POST.get('fname')
        b = req.POST.get('lname')
        c = req.POST.get('coun')
        d = req.POST.get('address')
        e = req.POST.get('city')
        f = req.POST.get('pin')
        g = req.POST.get('phone')
        h = req.POST.get('email')
        obj = CheckoutDB(FirstName=a, LastName=b, Country=c, Address=d, City=e, Pincode=f, Phonenumber=g, Emailaddress=h)
        obj.save()
        messages.success(req, "Saved checkout successfully")
        return redirect(homepage)
