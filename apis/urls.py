from django.urls import path,include
from apis.views import UserViewSet,demoViewSet
from . import views
from rest_framework import routers,serializers, viewsets
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
# router.register('farmeroffers',UserViewSet)
router.register(r'users', views.UserViewSet,basename="user")
router.register(r'demojoin', views.demoViewSet,basename="demo")
router.register(r'farmer/get/certificateid', views.farmercertificatebyidViewSet,basename="farmlistbyid")

urlpatterns=[
    path('',include(router.urls)),
    # path('user/get',views.UserViewSet),
    path('user/save',views.saveuser),
    path('user/profile',views.userprofile),
    path('user/login',views.loginuser),
    path('users/demo',views.UserViewdemoSet),
    path('roles/get',views.Roleget),
    path('product/get',views.Productget),
    path('add/farmer/offer',views.savefarmeroffers),
    path('add/buyer/offer',views.saveBuyeroffers),
    path('farmer/offer/list',views.allfarmerofferlist),
    path('farmer/offer/list/<int:id>/',views.farmerofferlistbyid),
    path('buyer/offer/list',views.allbuyerofferlist),
    path('buyer/offer/list/<int:id>',views.buyerofferlistbyid),
    path('abc',views.demoaaabcd),
    # path('farmer/get/certificateid/<int:id>',views.getfarmercertificatebyid),
]

