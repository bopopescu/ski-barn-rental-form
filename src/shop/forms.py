from django import forms
from .models import serviceTicket, mountTicket

class serviceForm(forms.ModelForm):
    class Meta:
        model = serviceTicket
        fields = ['user', 'req_date', 'ski_model', 'ski_make', 'binding_model', 'binding_make', 'boot_model', 'boot_make', 'service','comments',]

class skiMountForm(forms.ModelForm):
    class Meta:
        model = mountTicket
        fields = ['user', 'first_name', 'last_name', 'height_inches', 'weight', 'age', 'skiier_type', 'req_date', 'ski_model', 'ski_make', 'binding_model', 'binding_make', 'boot_model', 'boot_make', 'service', 'comments',]

class boardMountForm(forms.ModelForm):
    class Meta:
        model = mountTicket
        fields = ['user', 'first_name', 'last_name', 'height_inches', 'weight', 'age', 'stance', 'req_date', 'ski_model', 'ski_make', 'binding_model', 'binding_make', 'boot_model', 'boot_make', 'service', 'comments',]