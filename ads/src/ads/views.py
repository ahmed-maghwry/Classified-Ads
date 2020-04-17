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
def ff (request):
    main_ff = request.GET.get('mainff')
    if main_ff == "8" :
        cat=bbf()
    elif main_ff == "23" :
        cat=mobilef()
    else :
        cat="Ahmed"
    context2 ={

        'cat':cat,
    }
    
    return render (request , 'ff.html' , context2)


    #########################################################################
def creat_ads(request):
    
    if request.method =='POST':
        form = adsform(request.POST ,request.FILES)
        


        if form.is_valid() :
            print(1)
            new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
            new_form.user=request.user
            print(type(new_form.main.id))
            if new_form.main.id == 8 :
                catff = bbf (request.POST , request.FILES)
                print(3)
            elif new_form.main.id == 23 :
                print(4)
                catff = mobilef (request.POST , request.FILES)
            else :
                print(5)
                pass
            if catff.is_valid() :
                form.save()
                catff.save()
                return redirect('/')
            else : pass
    else:
        form = adsform()

    context = {
        'form': form ,
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
