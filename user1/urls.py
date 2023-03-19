# urls.py
from django.urls import path

from . import views
app_name = "user1"
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('create/', views.create, name='create'),
    path('orderlaundry/', views.OrderLaundry.as_view(), name='orderlaundry')
]