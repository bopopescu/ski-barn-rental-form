from django.db import models
from accounts.models import User
from datetime import date
from django.db.models.functions import Now
import datetime

class renter(models.Model):
    renter_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique = False, blank = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    genders = [
        [True,'Male'],
        [False,'Female'],
    ]
    gender = models.BooleanField(choices = genders, default = True)
    Dob = models.DateField(auto_now=False,auto_now_add=False,)
    def location(self):
        location = UserInfo.objects.get(pk = user).location
        return location
    def age(self):
        today = date.today()
        birthday = self.Dob
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    def full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name
    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name
class rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    renter = models.ForeignKey(renter, on_delete=models.CASCADE, unique = False)
    height_inches = models.IntegerField()
    weight = models.IntegerField()
    equipment =[
        [True,'Ski'],
        [False,'Snowboard'],
    ]
    using = models.BooleanField(default=True, choices=equipment)
    stances = [
        [-1 ,  'None'],
        [1, 'Regular'],
        [0, 'Goofy'],
    ]
    stance = models.IntegerField(default=True, choices=stances, blank = True)
    ski_types = [
        [0, 'None'],
        [1, 'Type 1'],
        [2, 'Type 2'],
        [3, 'Type 3'],
    ]
    ski_type = models.IntegerField(default = 1, choices = ski_types, null = True)
    input_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        info = self.renter.first_name + ' ' + self.renter.last_name
        return info