from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ads(models.Model):
    options =( 
    ("ex", "ex"), 
    ("Sale", "Sale"), 
    ("free", "free"), 
    ) 

    user = models.ForeignKey(User, blank=True , null=True, on_delete=models.CASCADE)
    # slug= models.SlugField(default='' , null = True , blank= True)
    title =models.CharField(max_length=80)
    description = models.TextField(max_length=500,default='')
    create_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    view =models.IntegerField(default=0)
    ad_option = models.CharField(max_length=4, choices=options , default='ex')
    img=models.ImageField(upload_to='post_img/' , default="img/defu.png")
    name_of_who=models.CharField(max_length=15 , null=True,blank=True)
    adress=models.CharField(max_length=80 , null=True,blank=True)
    mobile =models.PositiveSmallIntegerField( default=1114796307 , null=True,blank=True,)
    email=models.EmailField(default="ahmed_mag22@yahoo.com" , null=True,blank=True)



    class Meta:
        ordering = ['-view']
    def __str__(self):
        return self.title


class car_cat(models.Model):
    cat_name=models.CharField ( max_length=15)
    cat_main=models.ForeignKey ( 'self' , related_name='prod_category_set', 
                                limit_choices_to={'cat_main__isnull':True},
                                on_delete=models.CASCADE,blank=True,null=True)
    # cat_Sub=models.ForeignKey ( 'self' , related_name='prod_sub_category_set',
    #                             limit_choices_to={'cat_Sub__isnull':True ,
    #                                               'cat_main__isnull':False }
    #                             ,on_delete=models.CASCADE,blank=True,null=True)
    # cat_desc=models.TextField()


                                #  limit_choices_to={'cat_main__isnull':True
                                #      ,'cat_Sub__isnull':True}
                                #  , 

    def __str__(self):
        return self.cat_name


class mop_cat(models.Model):
    cat_name=models.CharField ( max_length=15)
    cat_main=models.ForeignKey ( 'self' , related_name='prod_category_set', 
                                limit_choices_to={'cat_main__isnull':True},
                                on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.cat_name