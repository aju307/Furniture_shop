from django.shortcuts import render, redirect
from backend.models import catDB,Productdb,Contact
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate


# Create your views here.
def indexpage(req):
    return render(req, 'index.html')


def addcategory(req):
    return render(req, 'addcategory.html')


def savedata(req):
    if req.method == "POST":
        n = req.POST.get('name')
        d = req.POST.get('description')
        i = req.FILES['image']
        obj = catDB(Catogory_name=n, Description=d, Image=i)
        obj.save()
        return redirect(addcategory)


def displaycategory(req):
    data = catDB.objects.all()
    return render(req, 'displaycategory.html', {'data': data})

def editecatogory(req,dataid):
    cat = catDB.objects.get(id=dataid)
    return render(req, 'editecategory.html', {'cat':cat})

def updatecatogery(req,dataid):
    if req.method=="POST":
        n=req.POST.get('name')
        d=req.POST.get('description')
        try:
            img=req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= catDB.objects.get(id=dataid).Image
        catDB.objects.filter(id=dataid).update(Catogory_name=n,Description=d,Image=file)
        return redirect(displaycategory)


def deletecatogory(req,dataid):
    data = catDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)


def addproduct(req):
    catogory=catDB.objects.all()
    return render(req,'addproduct.html',{'catogory':catogory})
def saveproductdata(req):
    if req.method == "POST":
        c = req.POST.get('cat')
        n = req.POST.get('name')
        d = req.POST.get('description')
        p = req.POST.get('price')
        i = req.FILES['image']
        obj1 = Productdb(Product_name=n,Description=d,Price=p,Image=i,Catogory_name=c)
        obj1.save()
        return redirect(addproduct)
def displayproduct(req):
    product = Productdb.objects.all()
    return render(req,'displayproduct.html',{'product':product})
def editpdt(request,dataid):
    category = catDB.objects.all()
    data = Productdb.objects.get(id=dataid)
    return render(request,"editproduct.html",{'category':category,'data':data})

def updatepdt(request,dataid):
    if request.method == "POST":
        c = request.POST.get('cat')
        bn = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')

        try:
            img = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=dataid).Image
        Productdb.objects.filter(id=dataid).update(Product_name=bn,Description=desc,Price=price,Image=file,Catogory_name=c)
        return redirect(displayproduct)

def deletepdt(req,dataid):
    data = Productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)


def admin_login(request):
    return render(request,"admin_login.html")

def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pas')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(indexpage)
            else:
                return redirect(admin_login)
        else:
            return redirect(admin_login)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)
def viewcontact(req):
    data = Contact.objects.all()
    return render(req,"viewcontact.html",{ 'data':data})
