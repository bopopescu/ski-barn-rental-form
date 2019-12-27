from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import serviceForm, skiMountForm, boardMountForm
from accounts.models import User
from .models import serviceTicket, mountTicket

def shopMain(request, account_id):
    u = User.objects.get(pk = account_id)
    if 'start' in request.META['PATH_INFO']:
        return render(request, 'shop/makeTicket.html',{'account_id':account_id})
    elif 'view' in request.META['PATH_INFO']:
        st = None
        mt = None
        try:
            st = serviceTicket.objects.filter(user = account_id)
        except serviceTicket.DoesNotExist:
            try:
                mt = mountTicket.objects.filter(user = account_id)
            except mountTicket.DoesNotExist:
                if st == None:
                    return HttpResponseRedirect('/shop/1/startService/')
                else:
                    pass
        tickets = (mt, st)
        return render(request, 'shop/viewTickets.html',{'account_id':account_id, 'tickets': tickets})

def shopMount(request, account_id):
    return render(request, 'shop/mountStart.html', {'account_id':account_id,})

def skiMount(request, account_id):
    if request.method == 'POST':
        form = skiMountForm(request.POST)
        form.save()
    else:
        form = skiMountForm()
        return render(request, 'shop/skiMount.html',{'account_id':account_id, 'form':form})

def boardMount(request, account_id):
    if request.method == 'POST':
        form = boardMountForm(request.POST)
        form.save()
    else:
        form = boardMountForm()
        return render(request, 'shop/boardMount.html',{'account_id':account_id, 'form':form})