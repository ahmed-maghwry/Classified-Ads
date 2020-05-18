from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from . models import ads ,catugry , car_form
from . forms import carf , mobilef , adsform  ,car_forms ,adsform2
from django.urls import reverse_lazy



def edit_ads(request , id ):
    ads_edit=get_object_or_404(ads,id=id)
    signalf=0
    if request.method =='POST':
        form = adsform(request.POST , request.FILES, instance=ads_edit  )
        if form.data['main'] == "43" :
            try:
                ads_exe_edit=get_object_or_404(car_form,ad_id=ads_edit)
                catff = car_forms ( request.POST ,instance=ads_exe_edit )
                signalf=1
            except :   
                catff = car_forms ( request.POST )
                signalf=1     
            
        elif ads_edit.main.id == 43 and form.data['main'] == "43":
            pass
        else : 
            pass
        if signalf == 1 :
            if form.is_valid() and catff.is_valid() :
                new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                new_form.user=request.user
                new_catff=catff.save(commit=False)
                new_catff.ad_id=form.save()
                try : ads_exe_edit.delete()
                except:pass
                form.save()
                catff.save()   
                return redirect('/')
                
            else:
                main_id_creat=form.data['main']
                sub_id_creat=form.data['sub']
                end_id_creat=form.data['end']
                if main_id_creat == "" : main_id_creat=0
                else: main_id_creat=form.data['main']
                if sub_id_creat == "" : sub_id_creat=0
                else: sub_id_creat=form.data['sub']
                if end_id_creat == "" : end_id_creat=0
                else: end_id_creat=form.data['end']
                form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_creat , sub_id=None
                ).order_by('name')
                form.fields['end'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=None).order_by('name')
                form.fields['last'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=end_id_creat
                ).order_by('name')
                context = {
                    'form': form,
                    'catff': catff,
                    'signalf': signalf,
                }
                pass
        else:
            if ads_edit.main.id == 43 :
                try :
                    ads_exe_edit=get_object_or_404(car_form,ad_id=ads_edit)
                except:pass
                if form.is_valid() :
                    new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                    new_form.user=request.user
                    form.save()
                    try : ads_exe_edit.delete()
                    except:pass
                    return redirect('/')
                else:
                    main_id_creat=form.data['main']
                    sub_id_creat=form.data['sub']
                    end_id_creat=form.data['end']
                    if main_id_creat == "" : main_id_creat=0
                    else: main_id_creat=form.data['main']
                    if sub_id_creat == "" : sub_id_creat=0
                    else: sub_id_creat=form.data['sub']
                    if end_id_creat == "" : end_id_creat=0
                    else: end_id_creat=form.data['end']
                    form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_creat , sub_id=None
                    ).order_by('name')
                    form.fields['end'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=None).order_by('name')
                    form.fields['last'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=end_id_creat
                    ).order_by('name')
            else:
                if form.is_valid() :
                    new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                    new_form.user=request.user
                    form.save()
                    return redirect('/')
                else:
                    main_id_creat=form.data['main']
                    sub_id_creat=form.data['sub']
                    end_id_creat=form.data['end']
                    if main_id_creat == "" : main_id_creat=0
                    else: main_id_creat=form.data['main']
                    if sub_id_creat == "" : sub_id_creat=0
                    else: sub_id_creat=form.data['sub']
                    if end_id_creat == "" : end_id_creat=0
                    else: end_id_creat=form.data['end']
                    form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_creat , sub_id=None
                    ).order_by('name')
                    form.fields['end'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=None).order_by('name')
                    form.fields['last'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=end_id_creat
                    ).order_by('name')

            
    else:
        form= adsform(instance=ads_edit )
        main_id_creat=ads_edit.main
        sub_id_creat=ads_edit.sub
        end_id_creat=ads_edit.end
        if main_id_creat == "" or main_id_creat == None: 
            main_id_creat=0
            form.fields['sub'].queryset = catugry.objects.none()
            form.fields['end'].queryset = catugry.objects.none()
            form.fields['last'].queryset = catugry.objects.none()
        else: main_id_creat=ads_edit.main
        if sub_id_creat == "" or sub_id_creat == None:
            sub_id_creat=0
            form.fields['end'].queryset = catugry.objects.none()
            form.fields['last'].queryset = catugry.objects.none()
        else: sub_id_creat=ads_edit.sub
        if end_id_creat == "" or end_id_creat == None: 
            end_id_creat=0
            form.fields['last'].queryset = catugry.objects.none()
        else: end_id_creat=ads_edit.end
        form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_creat , sub_id=None
        ).order_by('name')
        form.fields['end'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=None).order_by('name')
        form.fields['last'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=end_id_creat
        ).order_by('name') 
        
        if ads_edit.main.id == 43 :
            ads_exe_edit=get_object_or_404(car_form,ad_id=ads_edit)
            catff = car_forms ( instance=ads_exe_edit )
            signalf=1
        elif ads_edit.main.id == 43 :
            ads_exe_edit=get_object_or_404(car_form,ad_id=ads_edit)
            # catff = mobilef (request.POST, instance=ads_edit )  
            # signalf=1
            pass
        else : 
            pass

    try:
        context = {
            'form': form ,
            'catff': catff,
            'signalf': signalf,
        }
    except :
        context = {
        'form': form ,
        'signalf': signalf,
    }
    return render (request , 'creat.html' , context)

