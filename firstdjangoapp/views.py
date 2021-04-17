from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world!!!")

def second(request):
    return HttpResponse("Well, life is good!!! \n ExpressJS is actually better than this....   ")
