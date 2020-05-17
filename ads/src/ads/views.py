from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from . models import ads ,catugry , car_form
from . forms import carf , mobilef , adsform  ,car_forms ,adsform2
from django.views.generic import UpdateView
from django.urls import reverse_lazy
cat=""# Empty variable use like signal and i think it is not important but i'm afraid to delete it
# Create your views here.
def all_ads(request):
    ads_all=ads.objects.all()
    context = {
        'ads_all' : ads_all ,
    }
    return render(request , 'all.html' , context)
    #########################################################################
def ads_detail(request , id):   
    detail=get_object_or_404(ads , id=id)
    context={
        'detail':detail ,
    }
    return render(request,'detail.html', context)
    #########################################################################
    # THIS Function USE TO CHANGE THE EXTENSION FORMS FOR VARIABLE OPTIONS 
    # LIKE SOME FIELDS FOR CARS ADS AND ANTHER FOR MOBILE ADS AND FOR JOB ADS
        # FOR MORE DETAILS {CARS FIELDS :Model , Model Year ,Kilometers  , 
        # Transmission Type ,Body Type ,Engine Capacity (CC)}
    # FOR MORE DETAILS {MOPILE FIELDS :Brand , RAM , processor Model }
    ###############
    # HOW IT WORK #
    ###############
    # 1- make ajax Function to return the id of chosen category if we have it
    #    and that to selected The right fields for the chosen category 
    #    If the identifier is 8, then this means that the user chooses cars ads  
    #    and so on for each category number 
    # 2-and if the category doesn't have special fields then return signalf context as zero
    # finally  if signalf context == zero there are no special fields for this ad


def change_form (request):
    main_form_id = request.GET.get('main_form_id')
    if main_form_id == "43" :
        cat=car_forms()
    elif main_form_id == "23" :
        cat=mobilef()
    else :
        cat="Ahmed" # Empty variable use like signal and i think it is not important but i'm afraid to delete it
# Create your views here.
    context2 ={
        'cat':cat,
        'signalf' :0  #variable use like signal to make me actually know is there main_form_id variable come with response or not
    }
    return render (request , 'change_form.html' , context2)
    #########################################################################
def creat_ads(request):

    signalf=0
    if request.method =='POST':
        form = adsform(request.POST , request.FILES )
        if form.data['main'] == "43" :
            catff = car_forms (request.POST )
            signalf=1
        elif form.data['main'] == "43" :
            catff = mobilef (request.POST )  
            signalf=1
        else : 
            pass
        if signalf == 1 :
            if form.is_valid() and catff.is_valid() :
                new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                new_form.user=request.user
                new_catff=catff.save(commit=False)
                new_catff.ad_id=form.save()
                print (form.cleaned_data)
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
        form= adsform() 
        form.fields['sub'].queryset = catugry.objects.none()
        form.fields['end'].queryset = catugry.objects.none()
        form.fields['last'].queryset = catugry.objects.none()
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
    ##################################################  edit_ads  #######################













def edit_ads(request , id ):
    ads_edit=get_object_or_404(ads,id=id)
    signalf=0
    if request.method =='POST':
        form = adsform(request.POST , request.FILES, instance=ads_edit  )
        print("111111111111111111111")
        print(ads_edit.main.id)
        print(form.data['main'])
        # if ads_edit.main.id == 43 and
        if form.data['main'] == "43" :
            try:
                ads_exe_edit=get_object_or_404(car_form,ad_id=ads_edit)
                catff = car_forms ( request.POST ,instance=ads_exe_edit )
                signalf=1
            except :   
                catff = car_forms ( request.POST )
                signalf=1     
            
        elif ads_edit.main.id == 43 and form.data['main'] == "43":
            # catff = mobilef (request.POST, instance=ads_edit )  
            # signalf=1
            pass
        else : 
            pass
        if signalf == 1 :
            print("3333333333333333333333333")
            if form.is_valid() and catff.is_valid() :
                print("44444444444444444")
                new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                new_form.user=request.user
                new_catff=catff.save(commit=False)
                new_catff.ad_id=form.save()
                try :
                    ads_exe_edit.delete()
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
            # print("else")
            # print (ads_edit.main.id)
            if ads_edit.main.id == 43 :
                print("eeeeeeeeeeeee")
                try :
                    ads_exe_edit=get_object_or_404(car_form,ad_id=ads_edit)
                except:pass
                if form.is_valid() :
                    print("55555555")
                    new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                    new_form.user=request.user
                    form.save()
                    try :
                        ads_exe_edit.delete()
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
                    print("55555555")
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




                    # main_id_creat=form.data['main']
                    # sub_id_creat=form.data['sub']
                    # end_id_creat=form.data['end']
                    # form_main=form.data['main']
                    # form_sub=form.data['sub']
                    # form_end=form.data['end']
                    # tes(main_id_creat,sub_id_creat,end_id_creat,form_main,form_sub,form_end)
                    # print("done")

            
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
    #########################################################################

def load_sub(request):
    
    main_idt = request.GET.get('main')
    sub_idt = request.GET.get('sub')
    end_idt = request.GET.get('end')
    if main_idt :
        sub = catugry.objects.filter(main_id=main_idt , sub_id=None).order_by('name')
        end=[]
        last=[]
    else:
        sub=[]
        end=[]
        last=[]

    if sub_idt :
        end = catugry.objects.filter( main_id=main_idt ,sub_id=sub_idt ,end_id=None).order_by('name')
        sub=[]  
    else:
        end=[]
        last=[]
    if end_idt:
        last = catugry.objects.filter( main_id=main_idt ,sub_id=sub_idt ,end_id=end_idt).order_by('name')
        sub=[]
        end=[]
    else: 
        last=[]
    context={
        'sub': sub ,
        'end': end ,
        'last': last,

    }
    return render(request, 'load_sub_list_options.html',context)
