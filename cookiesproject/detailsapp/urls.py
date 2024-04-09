from django.urls import path
from .views import father_view,mother_view,results_view,name_view
urlpatterns=[path('father_view/',father_view,name='father_view'),
             path('mother_view/', mother_view, name='mother_view') ,
             path('results_view/',results_view,name='results_view'),
             path('name_view/',name_view,name='name_view'),
             ]