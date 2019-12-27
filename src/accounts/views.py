from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import signupForm, loginForm, UserInfoForm, resetForm
from .models import User, UserInfo
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password

def index(request):
    return render(request, 'account/index.html',{})

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        try:
            username = form.data.get('email')
            u = User.objects.get(email = username)
        except ObjectDoesNotExist:
            if form.is_valid():
                form = signupForm.save(form,commit=False)
                form.set_password(request.POST.get('password'))
                form.save()
                u = User.objects.get(email=request.POST.get('email'))
                login(request)
                return HttpResponseRedirect('/rentals/%s/accountInfo/change/' %User.objects.get(email=request.POST.get('email')).pk)
        else:
            username = 'An account with this email already exists.'
            return render(request, 'account/signup.html',{'form': form, 'signerr': username})    
    else:
        form =  signupForm()
        return render(request, 'account\signup.html', {'form': form})

def login(request):
    form = loginForm(request.POST)
    if request.method == 'POST':
        username = form.data.get('email')
        password = form.data.get('password')
        try:
            u = User.objects.get(email = username)
        except ObjectDoesNotExist:
            username = 'Invalid email!'
            return render(request, 'account/login.html',{'form': form, 'logerr': username})    
        if check_password(password, u.password):
            user = authenticate(username = username, password = password)
            auth_login(request, user)
            acc_id = User.objects.get(email = form.data.get('email')).pk
            if 'rentals' in request.META["PATH_INFO"]:
                return HttpResponseRedirect('/rentals/%s/' %acc_id)
            else:
                return HttpResponseRedirect('/shop/%s' %acc_id)
        else:
            password = 'Invalid password!'
            return render(request, 'account/login.html',{'form': form, 'logerr': password}) 
    return render(request, 'account/login.html',{'form': form})    

@login_required( login_url='/rentals/login/')
def home(request, account_id):
    if 'rentals' in request.META['PATH_INFO']:
        return render(request, 'account/home.html',{'account_id':account_id,})
    elif 'shop' in request.META['PATH_INFO']:
        return render(request, 'account/shopHome.html',{'account_id':account_id,})

def accountInfo(request, account_id):
    try:
        acc_info = UserInfo.objects.get(pk= account_id)
        return render(request, 'account/accountInfo.html',{'account_id':account_id, 'acc_info':acc_info,})
    except ObjectDoesNotExist:
        return redirect('/rentals/%s/accountInfo/change' %account_id)

def changeInfo(request, account_id):
    u = User.objects.get(pk= account_id)
    if request.method == 'POST':
        form = UserInfoForm(request.POST.copy())
        form.user = u
        UserInfo.objects.update_or_create( user = account_id, defaults = {'user' : form.user, 'address' : form.data['address'], 'city': form.data['city'], 'state':form.data['state'], 'zipCode':form.data['zipCode'], 'location':form.data['location'], 'phone' : form.data['phone']})
        User.objects.filter(account_id = account_id).update(UserInfo_id = account_id)
        if 'rentals' in request.META["PATH_INFO"]:
            return HttpResponseRedirect('/rentals/%s/' %account_id)
        elif 'shop' in request.META["PATH_INFO"]:
            return HttpResponseRedirect('/shop/%s/' %account_id)
 
    else:
        form =  UserInfoForm(initial = {'user':u})
        return render(request, 'account/ChangeInfo.html',{'account_id':account_id, 'form':form,})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/rentals/')

def reset(request):
    if request.method == 'POST':
        form = resetForm(request.POST)
        form.set_password(form.data.get('password'))
        User.objects.filter(email = form.data.get('email')).update(password = form.password)
        return HttpResponseRedirect('/rentals/login/')
    else:
        form = resetForm()
        return render(request, 'account/reset.html', {'form':form})