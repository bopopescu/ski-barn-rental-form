from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'landing'),
    path('signup/', views.signup, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('<int:account_id>/', views.home, name='home'),
    path('<int:account_id>/accountInfo/',views.accountInfo, name ='accountInfo'),
    path('<int:account_id>/accountInfo/change/', views.changeInfo, name = 'changeAccountInfo'),
    path('logout/', views.logout, name= 'logout'),
    path('<int:account_id>/renters/', include('rentals.urls')),
    path('reset/', views.reset, name = 'reset password'),
    path('<int:account_id>/startService/', include('shop.urls')),
    path('<int:account_id>/viewService/', include('shop.urls')),
]
