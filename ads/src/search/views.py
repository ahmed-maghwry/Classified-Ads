
from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from ads.models import ads ,catugry , car_form
from django.urls import reverse_lazy

def by_catugry(request ):
    catugry_1 = request.GET.get('cat')
    print(catugry_1)
    by_catugry_2=ads.objects.filter(main_id=catugry_1).order_by('title')
    context = {
        'by_catugry_2' : by_catugry_2 ,
    }
    return render(request, 'by_catugry.html',context)


    

