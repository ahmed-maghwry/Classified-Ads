from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from . models import ads ,catugry
from . forms import adsform



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

def creat_ads(request):
    from . forms import adsform

    if request.method =='POST':
        form = adsform(request.POST ,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
            new_form.user=request.user
            form.save()
            return redirect('/')
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
        # last=[]
    
    else: pass
        # sub =  catugry.objects.none()        
        # end =  catugry.objects.none()
        # last = catugry.objects.none()
    if end_idt:
        last = catugry.objects.filter( main_id=main_idt ,sub_id=sub_idt ,end_id=end_idt).order_by('name')
        sub=[]
        end=[]
        print ("ok")

    else: print ("else")
        # end = catugry.objects.none()
        # last = catugry.objects.none()
        # sub = catugry.objects.none()
    context={
        'sub': sub ,
        'end': end ,
        'last': last
    }
    return render(request, 'load_sub_list_options.html',context)
