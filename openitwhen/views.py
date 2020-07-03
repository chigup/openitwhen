from django.http import HttpResponse
from django.shortcuts import render
from .models import Letters



def index(request):
    letter = Letters.objects.all()
    return render(request, 'index.html',{'letters': letter})




