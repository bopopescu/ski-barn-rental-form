from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, UserInfo
from rentals.models import renter

class UserInfoInline(admin.StackedInline):
    model = UserInfo

class renterInline(admin.StackedInline):
    model = renter

class userAdmin(admin.ModelAdmin):
    def phone(self, obj):
        return UserInfo.objects.get(pk = obj.account_id).phone
    def address(self, obj):
        return UserInfo.objects.get(pk = obj.account_id).address
    def location(self, obj):
        return UserInfo.objects.get(pk = obj.account_id).location
    list_display = ( 'email', 'last_login', 'phone', 'address', 'location',)
    search_fields = ('email', 'phone', 'address')
    inlines = [UserInfoInline, renterInline]

admin.site.unregister(Group)
admin.site.register(User, userAdmin)