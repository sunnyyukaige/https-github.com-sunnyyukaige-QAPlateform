from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(requests):
    return HttpResponse('hello sunny')

def login(request):
    return render(request,'login.html')