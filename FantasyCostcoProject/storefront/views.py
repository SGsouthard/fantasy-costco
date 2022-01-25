from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Fantasy Costco! Where all your dreams come true! Got a deal for you!")