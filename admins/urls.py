from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.login,name='login'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('admins/add/user/',views.adminuser,name='adminadduser'),
    path('admins/save/user/',views.adminsaveuser,name='saveadminuser'),
    path('admins/list/user/',views.adminuserlist,name='listadminuser'),
    path('logout/',views.logout,name='adminlogout'),
    path('dash/',views.dashboard,name='dashboard'),
    path('user/list/<int:id>',views.userlist,name='userlist'),
    path('user/add/',views.useradd,name='adduser'),
    path('saveuser/',views.savedemouser,name='saveuser'),
    path('user/edit/', views.edituser,name='edituser'),
    path('user/update/', views.updateuser,name='updateuser'),
    path('user/delete/', views.userdelete,name='userdelete'),
    path('user/byrole/<int:role>', views.userbyrole,name='userbyrole'),
    # path('logout/', views.logout,name='logout'),
    path('send_json/', views.send_json,name='send_json'),
    path('crop/add/', views.addcrop,name='cropadd'),
    path('crop/save/', views.savecrop,name='cropsave'),
    path('crop/list/', views.croplist,name='croplist'),
    # path('category/list/', views.categorylist,name='catlist'),
    path('profile/view/',views.profileview,name='profileview'),
    path('profile/update/',views.profileupdate,name='profileupdate'),
    path('product/add/', views.addproduct,name='addproduct'),
    path('product/save/', views.productsave,name='saveproduct'),
    path('product/list/', views.productlist,name='listproduct'),
    path('role/add/', views.addrole,name='addrole'),
    path('role/save/', views.rolesave,name='rolesave'),
    path('role/list/', views.listrole,name='listrole'),
    path('privacy/view/', views.privacy,name='privacy'),
    path('privacy/update/', views.updateprivacy,name='updateprivacy'),
    path('terms/view/', views.terms,name='terms'),
    path('terms/update/', views.updateterms,name='updateterms'),
    path('about/view/', views.aboutus,name='aboutus'),
    path('about/update/', views.updateaboutus,name='updateaboutus'),
    path('dtata/', views.dtata,name='dtata'),
    path('offer/details/<int:ids>', views.offerdetails,name='offerdetails'),
    path('payment/farmers', views.farmpayment,name='farmpayment'),
    path('payment/logistics', views.logistics,name='logistics'),
    path('fieldissue', views.farmerfield,name='farmerfield'),
    path('view/settings', views.adsettings,name='adsettings'),
    path('update/settings', views.updateadsettings,name='updateadsettings'),
    path('address', views.address,name='address'),
    path('getaddressbymap/<int:id>', views.getaddressbymap,name='getaddressbymap'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)