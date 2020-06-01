from django.shortcuts import get_object_or_404 , redirect
from ads.models import *
from django.shortcuts import render 
from .forms import * 


def change_form_search (request):
    range_price_form = price_form()
    sub_form_id = request.GET.get('subId')
    main_form_id = request.GET.get('mainId')
    forms_={
        '44' : car_search() , '46' : motorcycles_search() , '47' : car_spare_parts_search() ,
        '49' : Boats_search() , '48' : heavy_trucks_search() , '51' : mobile_phones_search() ,
        '50' : mobile_accessories_search()   
    }
    if sub_form_id in forms_ :
        main_form_search=forms_[sub_form_id]  
    else:main_form_search=''
    context2 ={
        'main_form_search':main_form_search,
        'range_price_form':range_price_form,
        'sub_form_id':sub_form_id,
    }
    return render (request , 'change_form_search.html' , context2)

def check_is_number(number):
    if number != '0'and number != "0.0" :
        try:
            if float (number):return True
        except:return False
    else :return False

def by_main_result(request):
    search_db_id = request.GET.get('sub')
    db_list={
            '':'no_form' , '44' : 'car', '46' : 'motorcycles' , '47' : 'car_spare_parts' ,
            '49' : 'Boats' , '48' : 'heavy_trucks' , '51' : 'mobile_phones' ,
            '50' : 'mobile_accessories'   
        }
    if check_is_number(search_db_id)==True :
        db_search=db_list[search_db_id]
    main_id_=43
    general_list=['sub' , 'end' ,'last']
    price_list=['to_Price', 'from_Price' ]
    signal=0
    if request.is_ajax():
        main_catugry_q=ads.objects.filter(main_id=main_id_ , sub_id=search_db_id)
        print(search_db_id)
        print(main_catugry_q)
        for search_key in request.GET :
            search_value=request.GET.get(search_key)
            if search_value != "" and search_value != None :
                search_value=request.GET.get(search_key)
                if search_key in general_list :
                    signal=1
                    search_var={search_key : search_value}
                    main_catugry_q=main_catugry_q.filter( ** search_var )
                elif  search_key not in general_list and search_key not in price_list and search_value != 'on' :
                    signal=1
                    exe_search_var="{}__{}__iexact".format(db_search ,search_key)
                    diction_search_var={exe_search_var:search_value}
                    main_catugry_q=main_catugry_q.filter(** diction_search_var )
                elif  search_key not in general_list and search_value == 'on' :
                    signal=1
                    bool_search_var="{}__{}__iexact".format(db_search ,search_key)
                    diction_bool_search_var={bool_search_var:'1'}
                    main_catugry_q=main_catugry_q.filter(** diction_bool_search_var )
                elif  search_key in price_list and check_is_number(search_value) == True  :
                    if search_key == 'from_Price'  :
                        signal=1
                        bool_search_var="{}__{}__gte".format(db_search , 'Price')
                        diction_bool_search_var={bool_search_var : search_value}
                        main_catugry_q=main_catugry_q.filter(** diction_bool_search_var )
                    elif search_key == 'to_Price' :
                        signal=1
                        bool_search_var="{}__{}__lt".format(db_search , 'Price')
                        diction_bool_search_var={bool_search_var : search_value}
                        main_catugry_q=main_catugry_q.filter(** diction_bool_search_var )
        if signal == 0 :
            main_catugry_q=ads.objects.filter(main_id=main_id_).order_by('-create_date')
    context = {'main_catugry_q' : main_catugry_q ,}
    return render(request, 'by_main_result.html',context)

