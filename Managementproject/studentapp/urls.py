from django.urls import path
from . import views

urlpatterns=[path('show/',views.show,name='show'),
             path('create/',views.create,name='create'),
             path('visual/',views.visual,name='visual')
             ]

