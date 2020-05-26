
from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from ads.models import ads ,catugry , car_form
from django.urls import reverse_lazy
from . forms import car_search , general
import json
import io

def by_catugry(request ):
    catugry_1 = request.GET.get('cat')
    if catugry_1 is not None or "" :
        by_catugry_2=ads.objects.filter(main_id=catugry_1).order_by('-create_date')
        context = {
            'by_catugry_2' : by_catugry_2 ,
        }
        return render(request, 'by_catugry.html',context)
    else:return HttpResponse("<h1>There are no object</h1>")




def by_main_properties(request , main_id_):
    main_id_=main_id_
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
    }
    return render(request, 'by_main_properties.html',context)
    # return HttpResponse("<h1>You Don't Have Permissio</h1>" )


def by_main_Sports(request , main_id_):
    main_id_=main_id_
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
    }
    return render(request, 'by_main_Sports.html',context)


def by_main_Babies(request , main_id_):
    main_id_=main_id_
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
    }
    return render(request, 'by_main_Babies.html',context)

def by_main_Vehicles(request , main_id_):
    general_search_form = general()
    car_search_form  =  car_search()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'car_search_form' : car_search_form , 

    }
    return render(request, 'by_main_Vehicles.html',context)

def by_main_Vehicles2(request):
    main_id_=43
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')    
    if request.is_ajax():
        print(request.GET.items)
        
        for key , value in request.GET.items():
            variable_column = key
            search_type = value
            filter = variable_column + '__' + search_type
            info=ads.filter(**{ filter: search_string })

            # main_catugry_q=ads.objects.filter( key == value ).order_by('-create_date')
            main_catugry_q=info
    context = {
        'main_catugry_q' : main_catugry_q ,
    } 
    return render(request, 'by_main_Vehicles2.html',context)





def by_main_Mobile(request , main_id_):
    main_id_=main_id_
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
    }
    return render(request, 'by_main_Mobile.html',context)

def by_main_clothes(request , main_id_):
    main_id_=main_id_
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
    }
    return render(request, 'by_main_clothes.html',context)
    

def by_main_Appliances(request , main_id_):
    main_id_=main_id_
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
    }
    return render(request, 'by_main_Appliances.html',context)


def by_main_Pets(request , main_id_):
    main_id_=main_id_
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
    }
    return render(request, 'by_main_Pets.html',context) 


def by_main_Electronic(request , main_id_):
    main_id_=main_id_
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
    }
    return render(request, 'by_main_Electronic.html',context)


def by_main_Services(request , main_id_):
    main_id_=main_id_
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
    }
    return render(request, 'by_main_Services.html',context)


def by_main_Furniture(request , main_id_):
    main_id_=main_id_
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
    }
    return render(request, 'by_main_Furniture.html',context)       