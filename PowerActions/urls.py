from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^ConnecttoDevice/', views.ConnecttoDevice, name="connect"),
    url(r'^poweroff/', views.PowerOffaDevice, name="off"),
    url(r'^powerOn/', views.PowerOnADevice, name="On"),
    url(r'^getdetails/',views.getdetails,name="details")
]
