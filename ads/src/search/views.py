
from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from ads.models import ads , catugry 
from django.urls import reverse_lazy
from . forms import *


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
    return render(request, 'by_main_properties.html',context)

def by_main_Sports(request , main_id_):
    general_search_form = general()
    car_search_form  =  car_search()
    range_price_form = price_form()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'car_search_form' : car_search_form , 
        'range_price_form': range_price_form ,
    }
    return render(request, 'by_main_Sports.html',context)


def by_main_Babies(request , main_id_):
    general_search_form = general()
    car_search_form  =  car_search()
    range_price_form = price_form()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'car_search_form' : car_search_form , 
        'range_price_form': range_price_form ,
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

def by_main_Mobile(request , main_id_):
    general_search_form = general()
    main_search_form  =  mobile_phones_search()
    range_price_form = price_form()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'main_search_form' : main_search_form , 
        'range_price_form': range_price_form ,
    }
    return render(request, 'by_main_Mobile.html',context)

def by_main_clothes(request , main_id_):
    general_search_form = general()
    car_search_form  =  car_search()
    range_price_form = price_form()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'car_search_form' : car_search_form , 
        'range_price_form': range_price_form ,
    }
    return render(request, 'by_main_clothes.html',context)
    

def by_main_Appliances(request , main_id_):
    general_search_form = general()
    car_search_form  =  car_search()
    range_price_form = price_form()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'car_search_form' : car_search_form , 
        'range_price_form': range_price_form ,
    }
    return render(request, 'by_main_Appliances.html',context)


def by_main_Pets(request , main_id_):
    general_search_form = general()
    car_search_form  =  car_search()
    range_price_form = price_form()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'car_search_form' : car_search_form , 
        'range_price_form': range_price_form ,
    }
    return render(request, 'by_main_Pets.html',context) 


def by_main_Electronic(request , main_id_):
    general_search_form = general()
    car_search_form  =  car_search()
    range_price_form = price_form()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'car_search_form' : car_search_form , 
        'range_price_form': range_price_form ,
    }
    return render(request, 'by_main_Electronic.html',context)


def by_main_Services(request , main_id_):
    general_search_form = general()
    car_search_form  =  car_search()
    range_price_form = price_form()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'car_search_form' : car_search_form , 
        'range_price_form': range_price_form ,
    }
    return render(request, 'by_main_Services.html',context)


def by_main_Furniture(request , main_id_):
    general_search_form = general()
    car_search_form  =  car_search()
    range_price_form = price_form()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()    
    main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {
        'main_catugry_q' : main_catugry_q ,
        'general_search_form' : general_search_form,
        'car_search_form' : car_search_form , 
        'range_price_form': range_price_form ,
    }
    return render(request, 'by_main_Furniture.html',context)       