from django.urls import path
from .views import getcookies,checkcookies,index

urlpatterns = [path('',index,name='index'),
                path('getcookies/',getcookies,name='getcookies'),
               path('checkcookies/',checkcookies,name='checkcookies')]