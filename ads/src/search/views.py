
from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from ads.models import ads ,catugry , car_form
from django.urls import reverse_lazy
from . forms import car_search , general , price_form
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
    return render(request, 'by_main_Vehicles.html',context)
def check_is_number(number):
    if number != '0'and number != "0.0" :
        try:
            if float (number):return True
        except:return False
    else :return False
def by_main_Vehicles2(request):
    main_id_=43
    general_list=['sub' , 'end' ,'last']
    price_list=['to_Price', 'from_Price' ]
    signal=0
    if request.is_ajax():
        for search_key in request.GET :
            search_value=request.GET.get(search_key)
            if search_value != "" and search_value != None :
                search_value=request.GET.get(search_key)
                if search_key in general_list :
                    signal=1
                    search_var={search_key : search_value}
                    main_catugry_q=ads.objects.filter( ** search_var )
                elif  search_key not in general_list and search_key not in price_list and search_value != 'on' :
                    signal=1
                    exe_search_var="car_form__{}__iexact".format(search_key)
                    diction_search_var={exe_search_var:search_value}
                    main_catugry_q=ads.objects.filter(** diction_search_var )
                elif  search_key not in general_list and search_value == 'on' :
                    signal=1
                    bool_search_var="car_form__{}__iexact".format(search_key)
                    diction_bool_search_var={bool_search_var:'1'}
                    main_catugry_q=ads.objects.filter(** diction_bool_search_var )
                elif  search_key in price_list and check_is_number(search_value) == True  :
                    if search_key == 'from_Price'  :
                        signal=1
                        bool_search_var="car_form__{}__gte".format('Price')
                        diction_bool_search_var={bool_search_var : search_value}
                        main_catugry_q=ads.objects.filter(** diction_bool_search_var )
                    elif search_key == 'to_Price' :
                        signal=1
                        bool_search_var="car_form__{}__lt".format('Price')
                        diction_bool_search_var={bool_search_var : search_value}
                        main_catugry_q=ads.objects.filter(** diction_bool_search_var )
        if signal == 0 :
            print('iiiiiiii')
            main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {'main_catugry_q' : main_catugry_q ,}
    return render(request, 'by_main_Vehicles_result.html',context)


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