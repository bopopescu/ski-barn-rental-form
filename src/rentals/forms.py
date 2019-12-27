from django import forms
from .models import renter, rental

class RenterForm(forms.ModelForm):
    class Meta:
        model = renter
        fields = ['user','first_name','last_name','gender','Dob']

class RentalForm(forms.ModelForm):
    class Meta:
        model = rental
        fields = ['renter','height_inches','weight','using','stance','ski_type']
    def __init__(self, account_id, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        self.fields['renter'].queryset = renter.objects.filter(user=account_id)