from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from . models import *
from . forms import *
from django.urls import reverse_lazy


def check_is_number(number):
    if number != '0'and number != "0.0":
        try:
            if float(number):
                return True
            else:
                pass
        except:
            return False
    else:
        return False


def edit_ads(request, id):
    ads_edit = get_object_or_404(ads, id=id)
    signalf = 0
    if request.method == 'POST':
        form = adsform(request.POST, request.FILES, instance=ads_edit)
        sub_form_id = form.data['sub']
        forms_ = {
            '44': [db_car, car], '46': [db_motorcycles, motorcycles], '47': [db_car_spare_parts, car_spare_parts],
            '49': [db_Boats, Boats], '48': [db_heavy_trucks, heavy_trucks], '51': [db_mobile_phones, mobile_phones],
            '52': [db_mobile_accessories, mobile_accessories]
        }
        if sub_form_id in forms_ and check_is_number(sub_form_id) == True:
            details_form_no_request = forms_[
                sub_form_id][1]  # 1 in list is FORM
            details_db_request = forms_[sub_form_id][0]  # 0 in list is DB NAME
            try:
                # it is take model name not form
                ads_exe_edit = get_object_or_404(
                    details_db_request, ad_id=ads_edit)
                details_form = details_form_no_request(
                    request.POST, instance=ads_exe_edit)
                signalf = 1
            except:
                details_form = details_form_no_request(request.POST)
                signalf = 1
        else:
            signalf = 0
        if signalf == 1:
            try:
                if ads_edit.sub.id != '' or ads_edit.sub.id != None:
                    sub_instance_id = ads_edit.sub.id
                else:
                    pass
            except:pass
            if form.is_valid() and details_form.is_valid():
                # تاخير حفظ الفورم حتي تعديلها
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_details_form = details_form.save(commit=False)
                new_details_form.ad_id = form.save()
                try:
                    details_db_request = forms_[
                        str(sub_instance_id)][0]  # 0 in list is DB NAME
                    # it is take model name not form
                    ads_exe_old = get_object_or_404(
                        details_db_request, ad_id=ads_edit)
                    ads_exe_old.delete()
                except:
                    pass
                form.save()
                details_form.save()
                return redirect('/')
            else:
                main_id_creat = form.data['main']
                sub_id_creat = form.data['sub']
                end_id_creat = form.data['end']
                if main_id_creat == "":
                    main_id_creat = 0
                else:
                    main_id_creat = form.data['main']
                if sub_id_creat == "":
                    sub_id_creat = 0
                else:
                    sub_id_creat = form.data['sub']
                if end_id_creat == "":
                    end_id_creat = 0
                else:
                    end_id_creat = form.data['end']
                form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_creat, sub_id=None
                                                                     ).order_by('name')
                form.fields['end'].queryset = catugry.objects.filter(
                    main_id=main_id_creat, sub_id=sub_id_creat, end_id=None).order_by('name')
                form.fields['last'].queryset = catugry.objects.filter(main_id=main_id_creat, sub_id=sub_id_creat, end_id=end_id_creat
                                                                      ).order_by('name')
                context = {
                    'form': form,
                    'details_form': details_form,
                    'signalf': signalf,
                }
                pass
        else:
            try:
                if ads_edit.sub.id != '' or ads_edit.sub.id != None:
                    sub_instance_id = ads_edit.sub.id
                else:
                    pass
            except:
                pass
            if form.is_valid():
                # تاخير حفظ الفورم حتي تعديلها
                new_form = form.save(commit=False)
                new_form.user = request.user
                try:

                    details_db_request = forms_[
                        str(sub_instance_id)][0]  # 0 in list is DB NAME
                    # it is take model name not form
                    ads_exe_old = get_object_or_404(
                        details_db_request, ad_id=ads_edit)
                    ads_exe_old.delete()
                except:
                    pass
                form.save()
                return redirect('/')
            else:
                main_id_creat = form.data['main']
                sub_id_creat = form.data['sub']
                end_id_creat = form.data['end']
                if main_id_creat == "":
                    main_id_creat = 0
                else:
                    main_id_creat = form.data['main']
                if sub_id_creat == "":
                    sub_id_creat = 0
                else:
                    sub_id_creat = form.data['sub']
                if end_id_creat == "":
                    end_id_creat = 0
                else:
                    end_id_creat = form.data['end']
                form.fields['sub'].queryset = catugry.objects.filter(
                    main_id=main_id_creat, sub_id=None).order_by('name')
                form.fields['end'].queryset = catugry.objects.filter(
                    main_id=main_id_creat, sub_id=sub_id_creat, end_id=None).order_by('name')
                form.fields['last'].queryset = catugry.objects.filter(
                    main_id=main_id_creat, sub_id=sub_id_creat, end_id=end_id_creat).order_by('name')
    else:
        form = adsform(instance=ads_edit)
        main_id_creat = ads_edit.main
        sub_id_creat = ads_edit.sub
        end_id_creat = ads_edit.end
        if main_id_creat == "" or main_id_creat == None:

            main_id_creat = 0
            form.fields['sub'].queryset = catugry.objects.none()
            form.fields['end'].queryset = catugry.objects.none()
            form.fields['last'].queryset = catugry.objects.none()
        else:
            main_id_creat = ads_edit.main
        if sub_id_creat == "" or sub_id_creat == None:
            sub_id_creat = 0
            form.fields['end'].queryset = catugry.objects.none()
            form.fields['last'].queryset = catugry.objects.none()
        else:
            sub_id_creat = ads_edit.sub
        if end_id_creat == "" or end_id_creat == None:
            end_id_creat = 0
            form.fields['last'].queryset = catugry.objects.none()
        else:
            end_id_creat = ads_edit.end
        form.fields['sub'].queryset = catugry.objects.filter(
            main_id=main_id_creat, sub_id=None).order_by('name')
        form.fields['end'].queryset = catugry.objects.filter(
            main_id=main_id_creat, sub_id=sub_id_creat, end_id=None).order_by('name')
        form.fields['last'].queryset = catugry.objects.filter(
            main_id=main_id_creat, sub_id=sub_id_creat, end_id=end_id_creat).order_by('name')
        try:
            if ads_edit.sub.id != '' or ads_edit.sub.id != None:
                sub_instance_id = ads_edit.sub.id
                forms_ = {
                    '44': [db_car, car], '46': [db_motorcycles, motorcycles], '47': [db_car_spare_parts, car_spare_parts],
                    '49': [db_Boats, Boats], '48': [db_heavy_trucks, heavy_trucks], '51': [db_mobile_phones, mobile_phones],
                    '52': [db_mobile_accessories, mobile_accessories]
                }
                if str(sub_instance_id) in forms_ and check_is_number(sub_instance_id) == True:
                    details_form_no_request = forms_[
                        str(sub_instance_id)][1]  # 1 in list is FORM
                    details_db_request = forms_[
                        str(sub_instance_id)][0]  # 0 in list is DB NAME
                    try:
                        # it is take model name not form
                        ads_exe_edit = get_object_or_404(
                            details_db_request, ad_id=ads_edit)
                        details_form = details_form_no_request(
                            instance=ads_exe_edit)
                        signalf = 1
                    except:
                        pass
                else:
                    pass
            else:
                pass
        except:
            pass
    try:
        context = {
            'form': form,
            'details_form': details_form,
            'signalf': signalf,
        }
    except:
        context = {
            'form': form,
            'signalf': signalf,
        }
    return render(request, 'edit.html', context)
