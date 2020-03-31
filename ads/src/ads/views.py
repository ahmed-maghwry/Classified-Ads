from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from . models import ads

# Create your views here.

def all_ads(request):
    ads_all=ads.objects.all()

    context = {

        'ads_all' : ads_all ,
    }

    return render(request , 'all.html' , context)


def ads_detail(request , id):   
    detail=get_object_or_404(ads , id=id)

    context={
        'detail':detail ,
    }

    return render(request,'detail.html', context)
    