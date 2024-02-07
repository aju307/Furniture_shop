from django.shortcuts import render,redirect
from backend.models import catDB,Productdb,Contact
from myapp.models import Registration,CartDB,savecheckout


# Create your views here.



def home(req):
    cat = catDB.objects.all()
    return render(req, 'home.html',{'cat':cat})
def products(req):
    pro = Productdb.objects.all()
    return render(req,'products.html',{'pro':pro})
def single_product(req,proid):
    data = Productdb.objects.get(id = proid)

    return  render(req,'single_product.html',{'data':data})
def products_filtered(req,cat_name):
    data = Productdb.objects.filter(Catogory_name = cat_name)
    return render(req,'products_filtered.html', {'data':data})
def aboutus(req):
    return render(req,'aboutus.html')
def services(req):
    cat = catDB.objects.all()
    return render(req,'services.html',{'cat':cat})
def contactus(req):
    return render(req,'contactus.html')
def contactdata(request):
    if request.method == "POST":
        name = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        obj = Contact(First_Name=name,Last_Name=lname,Email=email,Message=msg)
        obj.save()
        return redirect(contactus)

def Reg(req):
    return render(req, 'Reg.html')

def regdata(request):


    if request.method == "POST":

        name = request.POST.get('name')
        mob = request.POST.get('mob')
        email = request.POST.get('email')
        user = request.POST.get('username')
        pas = request.POST.get('pas')
        obj = Registration(Name=name, Mobile=mob, Email=email, Username=user, Password=pas)
        obj.save()
        return redirect(Reg)
def loginpage(req):
    return render(req, "Reg.html")
def userlogin(req):
    if req.method == "POST":
        un = req.POST.get('loginus')
        pwd = req.POST.get("loginpwd")
        if Registration.objects.filter(Username=un, Password=pwd).exists():
            req.session['Username'] =un
            req.session['Password'] =pwd
            return redirect(home)
        else:
            return redirect(Reg)
    return redirect(Reg)
def logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(loginpage)
def single(request):
    return render(request,'single2.html')
def checkout(request,):
 subtotal = savecheckout.objects.all()
 return render(request,'checkout.html',{'subtotal':subtotal})




def savecart(request):
    if request.method == "POST":
        pr = request.POST.get('pname')
        qu = request.POST.get('qt')
        tp = request.POST.get('tp')

        obj = savecheckout(Product_name=pr,quantity=qu,totalPrice=tp)
        obj.save()
        return redirect(checkout)

def thankyou(request):
    return render(request,'thankyou.html')