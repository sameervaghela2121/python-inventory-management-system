from django.urls import path, include
from . import views as v
urlpatterns = [
    path('index/',v.Index,name='index'),
    path('invoice/',v.Invoice,name='invoice'),
    path('inventory/',v.Invent,name='inventory'),
    path('',v.Login,name='login'),
    path('logout/',v.Logout,name='logout'),

]