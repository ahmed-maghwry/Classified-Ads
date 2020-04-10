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
    main_id = request.GET.get('main')
    print("sds")
    print(main_id)
    sub = catugry.objects.filter(main_id=main_id , sub_id=None).order_by('name')
    return render(request, 'load_sub_list_options.html', {'sub': sub})

    