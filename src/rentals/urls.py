from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.renterIndex, name= 'renterIndex'),
    path('rentals/', views.makeRentals , name='makeRentals'),
    path('<int:renter_id>/', views.viewRentals, name= 'viewRental'),
    path('<int:renter_id>/<int:rental_id>/', views.rentalDetail, name = 'rentalDetail')
]