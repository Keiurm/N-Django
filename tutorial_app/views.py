from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    if "msg" in request.GET:
        msg = request.GET["msg"]
        res = "Query Parameter:" + msg
    else:
        res = "No Query Parameter"
    return HttpResponse(res)


def information(request, id, name, age):
    res = "Your name:{}, Your ID:{}, Your age:{}".format(name, id, age)
    return HttpResponse(res)
