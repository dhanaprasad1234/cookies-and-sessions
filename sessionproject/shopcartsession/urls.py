from django.urls import path
from .views import display_view,add_view

urlpatterns = [path('add_view/',add_view,name='add_view'),
               path('display_view/',display_view,name='display_view')]