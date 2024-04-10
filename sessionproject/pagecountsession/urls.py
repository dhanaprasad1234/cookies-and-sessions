from django.urls import path
from .views import page_count_view

urlpatterns=[path('page_count_view/',page_count_view,name='page_count_view')]