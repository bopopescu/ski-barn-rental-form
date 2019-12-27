from django.contrib import admin
from .models import renter, rental
from accounts.models import User, UserInfo
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import render
from django.contrib.admin import ModelAdmin, SimpleListFilter

class rentalLocationFilter(admin.SimpleListFilter):
    title = 'Locations'
    parameter_name = 'location'
    def lookups(self, request, model_admin):
        return (
            (1, 'Paramus'),
            (2, 'Wayne'),
            (3, 'Shrewsbury'),
            (4, 'Lawrenceville'),
        )
    def queryset(self, request, queryset):
        if self.value() == None:
            return queryset
        ui = UserInfo.objects.filter(location = self.value()).values('user_id')
        r = queryset.filter(renter__user_id__in = ui)

        print (r, self.value())
        return r

class rentalAdmin(admin.ModelAdmin):
    def name(self, obj):
        name = obj.renter.first_name + ' ' + obj.renter.last_name
        return name
    def email(self, obj):
        return obj.renter.user.email
    def phone(self, obj):
        return UserInfo.objects.get(pk = obj.renter.user.account_id).phone
    def address(self, obj):
        return UserInfo.objects.get(pk = obj.renter.user.account_id).address
    def location(self, obj):
        return UserInfo.objects.get(pk = obj.renter.user.account_id).location
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:act_id>/print/',
                self.admin_site.admin_view(self.showRentalForm),
                name='Print',
            ),
        ]
        return custom_urls + urls
    def Print(self, obj):
        rnt_id = obj.rental_id
        return format_html(
            '<a class="button" href="%s/print/">Print</a>'%rnt_id
        )
    def showRentalForm(self, obj, act_id):
        rentalInst = rental.objects.get(pk = act_id)
        rentalInst.height_feet = rentalInst.height_inches//12
        rentalInst.height_inches = rentalInst.height_inches%12
        renterInst = renter.objects.get(pk = rentalInst.renter_id)
        userInst = User.objects.get(account_id =renterInst.user_id)
        userInfoInst = UserInfo.objects.get(pk = userInst.account_id)
        return render(obj, 'rentals/printPreview.html',
        {'rental':rentalInst, 'renter':renterInst, 'user': userInst,'userInfo':userInfoInst,})
    list_display = ('name', 'input_date', 'email', 'phone', 'address', 'location', 'Print')
    search_fields = ('renter__first_name', 'renter__last_name', 'renter__user__email', 'renter__user__UserInfo__phone', 'renter__user__UserInfo__address', 'input_date')
    list_filter = ('input_date', rentalLocationFilter,)
    def get_actions(self, request):
        actions = super(rentalAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
admin.site.register(rental, rentalAdmin)
admin.site.site_header = "Ski Barn Admin Site"
admin.site.site_title = "Ski Barn Admin Portal"
admin.site.index_title = "Welcome to Ski Barn Admin Portal"
ModelAdmin.show_full_result_count = False