from django.urls import path
from .views import  MerchList

urlpatterns = [
   path('api/merch', MerchList.as_view())
]