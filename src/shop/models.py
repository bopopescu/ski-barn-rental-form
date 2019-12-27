from django.db import models
from accounts.models import User


class serviceTicket(models.Model):
    input_date = models.DateTimeField(auto_now_add = True)
    req_date = models.DateTimeField()
    pickup_date = models.DateTimeField(blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique = False)
    ski_model = models.CharField(max_length = 45, blank = True)
    ski_make = models.CharField(max_length = 75, blank = True)
    binding_model = models.CharField(max_length = 45, blank = True)
    binding_make = models.CharField(max_length = 75, blank = True)
    boot_model = models.CharField(max_length = 45, blank = True)
    boot_make = models.CharField(max_length = 75, blank = True)
    services = [
        ['css','Complete Shop Service'],
        ['sws', 'Sharpen Wax Service'],

        ['other' ,'Other'],

    ]
    service = models.CharField(max_length = 20, choices = services)
    comments = models.TextField(blank = True)

class mountTicket(models.Model):
    input_date = models.DateTimeField(auto_now_add = True)
    req_date = models.DateTimeField()
    pickup_date = models.DateTimeField(blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique = False)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField (max_length = 100)
    height_inches = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    types = [
        [1, 'Type 1'],
        [2, 'Type 2'],
        [3, 'Type 3'],
    ]
    skiier_type = models.IntegerField( choices = types, blank = True)
    stances = [
        [True, 'Regular'],
        [False, 'Goofy'],
    ]
    stance = models.BooleanField(choices = stances, blank = True)
    ski_model = models.CharField(max_length = 45)
    ski_make = models.CharField(max_length = 75)
    binding_model = models.CharField(max_length = 45)
    binding_make = models.CharField(max_length = 75)
    boot_model = models.CharField(max_length = 45)
    boot_make = models.CharField(max_length = 75)
    services = [
        ['css','Complete Shop Service'],
        ['sws', 'Sharpen Wax Service'],
        
        ['other', 'Other'],
    ]
    service = models.CharField(max_length = 20, choices = services, blank = True)
    comments = models.TextField(blank = True)

