from django.conf.urls import url
from . import views , by_main_result
from django.urls import path , include
app_name = 'search'



urlpatterns = [
    # url(r'^(?P<catugry_1>[\w-]+)/$',views.by_catugry, name='by_catugry') ,
    url(r'^$', views.by_catugry, name='by_catugry'),# <-- this one here #
    url(r'^main/properties/(?P<main_id_>\d+)$', views.by_main_properties , name='by_main_properties'),
    url(r'^main/Sports/(?P<main_id_>\d+)$', views.by_main_Sports , name='by_main_Sports'),
    url(r'^main/Babies/(?P<main_id_>\d+)$', views.by_main_Babies , name='by_main_Babies'),
    url(r'^main/Vehicles/(?P<main_id_>\d+)$', views.by_main_Vehicles , name='by_main_Vehicles'),
    url(r'main/Vehicles/ajax/', by_main_result.by_main_result , name='by_main_result'),
    url(r'main/change_form/ajax/', by_main_result.change_form_search , name='change_form_search'),

    url(r'^main/Mobile/(?P<main_id_>\d+)$', views.by_main_Mobile , name='by_main_Mobile'),
    url(r'^main/clothes/(?P<main_id_>\d+)$', views.by_main_clothes , name='by_main_clothes'),
    url(r'^main/Appliances/(?P<main_id_>\d+)$', views.by_main_Appliances , name='by_main_Appliances'),
    url(r'^main/Pets/(?P<main_id_>\d+)$', views.by_main_Pets , name='by_main_Pets'),
    url(r'^main/Electronic/(?P<main_id_>\d+)$', views.by_main_Electronic , name='by_main_Electronic'),
    url(r'^main/Services/(?P<main_id_>\d+)$', views.by_main_Services , name='by_main_Services'),
    url(r'^main/Furniture/(?P<main_id_>\d+)$', views.by_main_Furniture , name='by_main_Furniture'),


    # url(r'^$',views.all_ads, name='all_ads') ,
    # url(r'^(?P<id>\d+)$', views.ads_detail , name='ads_detail'),
    # url(r'^creat$', views.creat_ads , name='creat_ads'),
    # url('ajax/load-cities/', views.load_sub, name='load_sub'),# <-- this one here #
    # url('ajax/change_form/', views.change_form, name='change_form'),   # <-- this one here
    # url(r'^(?P<id>\d+)/edit$', edit.edit_ads, name='edit_ads'),
    # url(r'^$',views.all_post, name='all_post' ) ,
    # url(r'^del/(?P<id>\d+)$', views.del_post, name='del_post'),
    # url(r'^test$', views.test, name='test'),

]
