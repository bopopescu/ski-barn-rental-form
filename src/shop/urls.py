from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shopMain, name = 'shop'),
    path('mount/', views.shopMount, name = 'mount'),
    path('mount/ski/', views.skiMount, name = 'mount'),
    path('mount/board/', views.boardMount, name = 'mount'),

]