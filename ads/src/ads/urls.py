from django.conf.urls import url
from . import views
app_name = 'ads'


urlpatterns = [
     url(r'^$',views.all_ads, name='all_ads') ,
     
    # url(r'^(?P<id>\d+)$', views.details_product , name='details_product'),

    # url(r'^$',views.all_post, name='all_post' ) ,
    # url(r'^create$', views.create_post , name='create_post'),
    # url(r'^(?P<id>\d+)/edit$', views.edit_post, name='edit_post'),
    # url(r'^del/(?P<id>\d+)$', views.del_post, name='del_post'),
    # url(r'^test$', views.test, name='test'),

]
