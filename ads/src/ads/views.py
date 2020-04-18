from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from . models import ads ,catugry
from . forms import carf , mobilef , adsform , bbf



cat="Ahmed"
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
def change_form (request):
    main_ff = request.GET.get('mainff')
    if main_ff == "8" :
        cat=bbf()
    elif main_ff == "23" :
        cat=mobilef()
    else :
        cat="Ahmed"
    context2 ={

        'cat':cat,
        'signalf' :0
    }
    
    return render (request , 'change_form.html' , context2)


    #########################################################################
def creat_ads(request):
    signalf=0
    
    if request.method =='POST':
        print (" request is post")
        form = adsform(request.POST ,request.FILES)
        
        if form.data['main'] == "8" :
            print ("main = 8")
            catff = bbf (request.POST , request.FILES)
            catf22=bbf()
            signalf=1
        elif form.data['main'] == "23" :
            print ("main = 23")
            catff = mobilef (request.POST , request.FILES)  
            catf22=mobilef()
            signalf=1

        else : 
            print ("no main response")
            pass
        if signalf == 1 :
            print ("test main in response or not ")
            if form.is_valid() and catff.is_valid() :
                print ("test two form valid or not ")
                new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                new_form.user=request.user
                form.save()
                catff.save()
                return redirect('/')

            
            else:
                print ("return one of two forms is not valid")
                context = {
                    'form': form,
                    'catff': catff,
                    'signalf': signalf,
                }
                pass
        else:
            print (" main is not in response")
            if form.is_valid() :
                print ("if form is valid ")
                new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                new_form.user=request.user
                form.save()
                return redirect('/')
            else:
                print ("form is not valid")
                # form = adsform()
                pass
    else:
        print (" not POST request")
        form= adsform() 

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
    sub = catugry.objects.filter(main_id=main_idt , sub_id=None).order_by('name')
    end=[]
    last=[]
    if sub_idt :
        end = catugry.objects.filter( main_id=main_idt ,sub_id=sub_idt ,end_id=None).order_by('name')
        sub=[]
    
    else: pass
        # sub =  catugry.objects.none()        
        # end =  catugry.objects.none()
        # last = catugry.objects.none()
    if end_idt:
        last = catugry.objects.filter( main_id=main_idt ,sub_id=sub_idt ,end_id=end_idt).order_by('name')
        sub=[]
        end=[]

    else: pass
        # end = catugry.objects.none()
        # last = catugry.objects.none()
        # sub = catugry.objects.none()
    context={
        'sub': sub ,
        'end': end ,
        'last': last
    }
    return render(request, 'load_sub_list_options.html',context)
