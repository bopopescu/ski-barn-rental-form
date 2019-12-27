from django.shortcuts import render
from .models import renter, rental
from .forms import RenterForm, RentalForm
from django.http import HttpResponseRedirect
from accounts.models import User
import datetime

def renterIndex(request, account_id,):
    if request.method == 'POST':
        form = RenterForm(request.POST.copy())
        form.data['first_name'] = form.data['first_name'].capitalize()
        form.data['last_name'] = form.data['last_name'].capitalize()
        try:
            form = RenterForm.objects.get_or_create(form.data)
        except AttributeError:
            if form.is_valid():
                u = User.objects.get(pk= account_id)
                form = RenterForm.save(form,commit=False)
                form.user = u
                form.save()
        return HttpResponseRedirect('/rentals/%s/' %account_id)
    else:
        form =  RenterForm()
        try:
            acc_info = renter.objects.filter(user= account_id)
        except renter.DoesNotExist:
            acc_info = None
        return render(request, 'rentals/renterIndex.html',{'account_id':account_id, 'acc_info':acc_info, 'form':form,})

def makeRentals(request, account_id):
    if request.method == 'POST':
        form = RentalForm(account_id, request.POST)
        if form.is_valid():
            form = RentalForm.save(form,commit=False)
            form.save()
        return HttpResponseRedirect('/rentals/%s/' %account_id)
    else:
        form =  RentalForm(account_id)
        acc_info = renter.objects.filter(user= account_id)
        return render(request, 'rentals/makeRental.html',{'account_id':account_id, 'acc_info':acc_info, 'form':form,})

def viewRentals(request, account_id, renter_id):
        rental_info = rental.objects.filter(renter= renter_id)
        renter_info = renter.objects.get(pk = renter_id)
        return render(request, 'rentals/viewRental.html',{'account_id':account_id, 'renter_info': renter_info, 'rental_info':rental_info, 'renter_id':renter_id,})

def rentalDetail(request, account_id, renter_id, rental_id):
    #date = datetime.datetime(rental_year,rental_month,rental_day, rental_time_h, rental_time_m, rental_time_s)
    #print(date)
    rental_info = rental.objects.get(renter_id = renter_id, rental_id = rental_id)
    rental_info.height_feet = rental_info.height_inches//12
    rental_info.height_inches = rental_info.height_inches%12
    renter_info = renter.objects.get(pk = renter_id)
    return render(request, 'rentals/rentalDetail.html',{'account_id':account_id, 'renter_info': renter_info, 'renter_id':renter_id, 'rental_info':rental_info})
