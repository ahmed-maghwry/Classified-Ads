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


def load_sub(request):
    main_idt = request.GET.get('main')
    sub_idt = request.GET.get('sub')
    sub = catugry.objects.filter(main_id=main_idt , sub_id=None).order_by('name')
    print( main_idt , sub_idt)
    end=[]
    if sub_idt :
        end = catugry.objects.filter( main_id=main_idt ,sub_id=sub_idt ,end_id=None).order_by('name')
        print (end)
        sub=[]

        print( main_idt , sub_idt)
    else: 
        print("no")
        end = catugry.objects.none()
    context={
        'sub': sub ,
        'end': end
    }
    return render(request, 'load_sub_list_options.html',context)
# def load_end(request):
#     main_id = request.GET.get('main')
#     sub_id = request.GET.get('sub')
#     end = catugry.objects.filter(sub_id=sub_id ).order_by('name')
#     return render(request, 'load_sub_list_options.html', {'end': end})


    