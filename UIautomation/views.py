from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login

def test(requests):
    return HttpResponse('welcome')

def login(request):
    if request.POST:
        username=request.POST.get('username') or ''
        password=request.POST.get('password') or ''
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user']=username
            response=HttpResponseRedirect('/home/')
            return response
        else:
            return  render(request,'login.html',{'error':'username or password error'})
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')