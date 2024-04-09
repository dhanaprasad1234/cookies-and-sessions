from django.urls import path
from .views import home,date_time_view,result_views
urlpatterns = [path('home/',home,name='home'),
              path('date_time_view/',date_time_view,name='date_time_view'),
              path('result_views/',result_views,name='result_views'),]