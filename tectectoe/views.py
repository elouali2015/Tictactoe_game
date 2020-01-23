from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    #return request(request,"tectectoe/welcome.html")
    return HttpResponse("hello")