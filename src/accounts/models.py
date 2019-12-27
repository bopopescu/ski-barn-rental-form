from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
import datetime
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password = None):
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save( using=self._db)
        return user



class User(AbstractBaseUser):
    account_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 255, unique = True)
    last_login = models.DateField(auto_now = True)
    join_date = models.DateField(auto_now_add = True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    UserInfo = models.OneToOneField('UserInfo', on_delete=models.CASCADE, blank = True, related_name='+')

    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    states =[
        ['al','Alabama'],
        ['ak','Alaska'],
        ['az','Arizona'],
        ['ar','Arkansas'],
        ['ca','California'],
        ['co','Colorado'],
        ['ct','Connecticut'],
        ['de','Delaware'],
        ['fl','Florida'],
        ['ga','Georgia'],
        ['hi','Hawaii'],
        ['id','Idaho'],
        ['il','Illinois'],
        ['in','Indiana'],
        ['ia','Iowa'],
        ['ks','Kansas'],
        ['ky','Kentucky'],
        ['la','Louisiana'],
        ['me','Maine'],
        ['md','Maryland'],
        ['ma','Massachusetts'],
        ['mi','Michigan'],
        ['mn','Minnesota'],
        ['ms','Mississippi'],
        ['mo','Missouri'],
        ['mt','Montana'],
        ['ne','Nebraska'],
        ['nv','Nevada'],
        ['nh','New Hampshire'],
        ['nj','New Jersey'],
        ['nm','New Mexico'],
        ['ny','New York'],
        ['nc','North Carolina'],
        ['nd','North Dakota'],
        ['oh','Ohio'],
        ['ok','Oklahoma'],
        ['or','Oregon'],
        ['pa','Pennsylvania'],
        ['ri','Rhode Island'],
        ['sc','South Carolina'],
        ['sd','South Dakota'],
        ['tn','Tennessee'],
        ['tx','Texas'],
        ['ut','Utah'],
        ['vt','Vermont'],
        ['va','Virginia'],['wa','Washington'],
        ['wv','West Virginia'],
        ['wi','Wisconsin'],
        ['wy','Wyoming']  
    ]
    state = models.CharField(max_length=200, choices=states, default='nj')
    zipCode = models.CharField(max_length=12)
    locations = [
        [1,"Paramus"],
        [2,"Wayne"],
        [3,"Shrewsbury"],
        [4,"Lawrenceville"]
    ]
    location = models.IntegerField(choices=locations, default=1)
    phone = models.CharField(max_length=10,)
    class Meta:
        verbose_name_plural = "User Info"
    def __str__(self):
        info = User.objects.get(pk = self.user_id).email
        return info

