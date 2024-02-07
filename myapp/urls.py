from django.urls import path
from myapp import views
urlpatterns = [

    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('single_product/<int:proid>/',views.single_product,name='single_product'),
    path('products_filtered/<cat_name>/',views.products_filtered,name='products_filtered'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('services/',views.services,name='services'),
    path('contactus/',views.contactus,name='contactus'),
    path('contactdata/',views.contactdata,name='contactdata'),
    path('Reg/',views.Reg,name='Reg'),
    path('regdata/',views.regdata,name='regdata'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('logout/', views.logout, name="logout"),
    path('single/', views.single, name="single"),
    path('checkout/', views.checkout, name="checkout"),
    path('savecart/',views.savecart,name='savecart'),
    path('thankyou/',views.thankyou,name='thankyou'),
]