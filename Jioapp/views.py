from django.shortcuts import render, redirect
from Jioapp.models import CategoryDB, ProductDB
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Frontend.models import ContactDB
from django.contrib import messages

# Create your views here.
def indexpage(request):
    return render(request, "Index.html")
def addcategory(request):
    return render(request, "AddCategory.html")
def category_save(request):
    if request.method =="POST":
        a = request.POST.get('cname')
        b = request.POST.get('des')
        img = request.FILES['img']
        obj = CategoryDB(CName=a, Description=b, Image=img)
        obj.save()
        messages.success(request,"Category saved successfully")
        return redirect(addcategory)
def category_details(request):
    data = CategoryDB.objects.all()
    return render(request, "Category_details.html", {'data': data})
def catedit(request,c_id):
    cat = CategoryDB.objects.get(id=c_id)
    return render(request, "Category_edit.html", {'cat': cat})

def cat_update(request, c_id):
    if request.method=="POST":
        a = request.POST.get('cname')
        b = request.POST.get('des')
        try:
            img = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=c_id).Image
        CategoryDB.objects.filter(id=c_id).update(CName=a, Description=b, Image=file)
        return redirect(category_details)
def cat_delete(request,c_id):
    cat=CategoryDB.objects.filter(id=c_id)
    cat.delete()
    messages.error(request,"Delete!")
    return redirect(category_details)
#*********************************************************************************************************************
def addproduct(request):
    return render(request, "AddProduct.html")
def product_save(request):
    if request.method =="POST":
        a = request.POST.get('cname')
        b = request.POST.get('pname')
        c = request.POST.get('des')
        d = request.POST.get('price')
        img = request.FILES['img']
        obj = ProductDB(CName=a,PName=b, Description=c, Price=d, Image=img)
        obj.save()
        messages.success(request,"Product saved successfully")
        return redirect(addproduct)
def product_details(request):
    data =ProductDB.objects.all()
    return render(request, "Product_details.html", {'data': data})
def proedit(request,p_id):
    pro = ProductDB.objects.get(id=p_id)
    return render(request, "Product_edit.html", {'pro': pro})

def pro_update(request, p_id):
    if request.method=="POST":
        a = request.POST.get('cname')
        b = request.POST.get('pname')
        c = request.POST.get('des')
        d = request.POST.get('price')
        try:
            img = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=p_id).Image

        ProductDB.objects.filter(id=p_id).update(CName=a,PName=b, Description=c, Price=d, Image=file)
        return redirect(product_details)

def pro_delete(request,p_id):
    pro = ProductDB.objects.filter(id=p_id)
    pro.delete()
    messages.error(request,"Delete!")
    return redirect(product_details)
def adminloginpage(request):
    return render(request, "Adminlogin.html")
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                messages.success(request, "Welcome")
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(indexpage)
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect(adminloginpage)
        else:
            return redirect(adminloginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminloginpage)

def contact_display(request):
    data = ContactDB.objects.all()
    return render(request, "Contact_Display.html", {'data': data})

def contact_delete(request,co_id):
     ContactDB.objects.filter(id=co_id).delete()
     return redirect(contact_display)