from django.urls import path
from .views import mother_view,name_view,father_view,result_view

urlpatterns=[path('name_view/',name_view,name='name_view'),
             path('father_view/',father_view,name='father_view'),
             path('mother_view/',mother_view,name='mother_view'),
             path('result_view/',result_view,name='result_view')
             ]