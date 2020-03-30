from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from .models import ads

# Create your views here.

def all_ads(request):
    ad=ads.objects.all

    context = {

        'ad' : ad ,
    }

    return render(request , 'index.html' , context)
