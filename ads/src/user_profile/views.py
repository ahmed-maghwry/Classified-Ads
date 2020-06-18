from django.shortcuts import render ,HttpResponse
from django.shortcuts import get_object_or_404
from ads.models import ads
from .models import user_details


# Create your views here.

def favoret(request , id) :
    now_user=request.user
    user_detail=get_object_or_404(user_details , user=now_user)
    ads_fav=get_object_or_404(ads , id=id)
    if user_detail.favoret_ads.all().filter(id=id).exists() :
        user_detail.favoret_ads.remove(id)
    else :
        user_detail.favoret_ads.add(id)
    return HttpResponse("<h1>There are no object</h1>")

    

