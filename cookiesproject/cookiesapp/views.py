from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    request.session.set_test_cookie()
    return HttpResponse("hi,i am bow")


def getcookies(request):
    request.session.set_test_cookie()
    name = request.COOKIES["name"]
    return HttpResponse("yours emails is" + name)





def checkcookies(request):
    if request.session.test_cookie_worked():
        print("cookies is worked")
        response = HttpResponse('worked properly <a href= "getcookies" >click</a>')
        response.set_cookie('email','prasad@gmail.com')
        return response


def getcookies(request):
    name = request.COOKIES["name"]
    print("hi")
    return HttpResponse("yours emails is" + name)
