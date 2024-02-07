from django.urls import path
from backend import views
urlpatterns = [
    path('indexpage/',views.indexpage,name='indexpage'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('savedata/',views.savedata,name='savedata'),
    path('displaycategory/',views.displaycategory,name='displaycategory'),
    path('editecatogory/<int:dataid>/',views.editecatogory,name='editecatogory'),
    path('updatecatogery/<int:dataid>/',views.updatecatogery,name='updatecatogery'),
    path('deletecatogory/<int:dataid>/', views.deletecatogory, name='deletecatogory'),


    path('addproduct/',views.addproduct,name='addproduct'),
    path('saveproductdata/',views.saveproductdata,name='saveproductdata'),
    path('displayproduct/',views.displayproduct,name='displayproduct'),
    path('editpdt/<int:dataid>/', views.editpdt, name="editpdt"),
    path('updatepdt/<int:dataid>/', views.updatepdt, name="updatepdt"),
    path('deletepdt/<int:dataid>/', views.deletepdt, name="deletepdt"),


    path('admin_login/', views.admin_login, name="admin_login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('viewcontact/', views.viewcontact, name="viewcontact"),
]