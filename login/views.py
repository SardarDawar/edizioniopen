from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from .forms import signupinfo,logininfo,resetpassword,forgotpassword1,forgotpassword2
from .models import infor
from django.core.mail import EmailMessage
import random


def status(request):
    template = 'status.html'
    context = {}
    return render(request,template,context)

def login(request):
    template = 'entry.html'
    form = logininfo(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        a = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        if a is not None:
            auth.login(request,a)
            return redirect('/profile')
    return render(request,template,context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    template = 'signupentry.html'
    form = signupinfo(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        un = form.cleaned_data['username']
        objs = User.objects.all()
        for i in objs:
            if i.username == un:
                return redirect('/loggin')
        paypal = form.cleaned_data['paypal_url']
        a = User.objects.create_user(
            un,
            form.cleaned_data['email'],
            form.cleaned_data['password']
        )
        a.first_name = form.cleaned_data['first_name']
        a.last_name = form.cleaned_data['last_name']
        a.save()
        linkaccount(request,un,paypal)
        return redirect('/loggin')
    return render(request,template,context)

def changepass(request):
    template = 'entry.html'
    form = resetpassword(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        a = User.objects.get(username = request.user.username)
        a.set_password(form.cleaned_data['new_password'])
        a.save()
        return redirect('/')
    return render(request,template,context)

def forgot(request):
    template = 'entry.html'
    form = forgotpassword1(request.POST)
    if form.is_valid():
        a = form.cleaned_data['username']
        userobjs = User.objects.all()
        lis = []
        for i in userobjs:
            lis.append(i.username)
        if a not in lis:
            return redirect('/')
        b = User.objects.get(username = a)
        c = infor.objects.get(name = a)
        mail = EmailMessage(
            'Forgot password'
            'Your password change key is : ' + c.passwordkey,
            to = [b.email]
        )
        form = forgotpassword2(request.POST)
        if form.is_valid():
            d = form.cleaned_data['key_from_mail']
            e = form.cleaned_data['new_password']
            if d == c.passwordkey:
                c.passwordkey = randomizer()
                c.save()
                b.set_password(e)
                b.save()
                return redirect('/loggin')
            context = {'form':form}
            return render(request,template,context)
    context = {'form':form}
    return render(request,template,context)

def linkaccount(request,un,paypal):
    objs = infor.objects.all()
    for i in objs:
        if i.package == pack and i.name == None:
            i.passwordkey = randomizer()
            i.name = un
            i.paypal_url = paypal
            i.save()
            break
    return 

def randomizer():
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    c = ''
    for i in range(0,9):
        c = c + a[random.randint(0,len(a)-1)]
    return c