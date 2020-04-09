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
    title =models.CharField(max_length=80)
    description = models.TextField(max_length=500,default='')


    main=models.ForeignKey ( 'catugry',related_name='ad_main',
                            limit_choices_to={'main__isnull':True ,
                             'sub__isnull':True ,
                             'end__isnull':True }
                               , on_delete=models.CASCADE,blank=True,null=True)
    sub=models.ForeignKey ( 'catugry' ,related_name='ad_sub',
                            limit_choices_to={'sub__isnull':True ,
                                'main__isnull':False ,
                                 'end__isnull':True }
                                ,on_delete=models.CASCADE,blank=True,null=True)
    end=models.ForeignKey ( 'catugry' , related_name='ad_end',
                                limit_choices_to={'sub__isnull':False ,
                                                  'main__isnull':False }
                                ,on_delete=models.CASCADE,blank=True,null=True)



    create_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    view =models.IntegerField(default=0)
    ad_option = models.CharField(max_length=4, choices=options , default='ex')
    img=models.ImageField(upload_to='post_img/' , default="img/defu.png")
    name_of_who=models.CharField(max_length=15 , null=True,blank=True)
    adress=models.CharField(max_length=80 , null=True,blank=True)
    mobile =models.PositiveSmallIntegerField( default=1114796307 , null=True,blank=True,)
    email=models.EmailField(default="ahmed_mag22@yahoo.com" , null=True,blank=True)
    
    
    def save( self,*args,**kwargs ):
        if  self.sub  :
            self.main= self.sub.main

        if self.end :
            self.main=self.end.sub.main
            self.sub=self.end.sub
            
        super(ads, self).save(*args,**kwargs)




    class Meta:
        ordering = ['-view']
    def __str__(self):
        return self.title



class catugry(models.Model):
    name=models.CharField ( max_length=20)
    main=models.ForeignKey ( 'self', related_name='re_main' ,
                            limit_choices_to={'main__isnull':True ,
                             'sub__isnull':True ,
                             'end__isnull':True }
                               , on_delete=models.CASCADE,blank=True,null=True)
    sub=models.ForeignKey ( 'self' , related_name='re_sub',
                            limit_choices_to={'sub__isnull':True ,
                                'main__isnull':False ,
                                 'end__isnull':True }
                                ,on_delete=models.CASCADE,blank=True,null=True)
    end=models.ForeignKey ( 'self' , related_name='re_end',
                                limit_choices_to={'sub__isnull':False ,
                                                  'main__isnull':False }
                                ,on_delete=models.CASCADE,blank=True,null=True)


    def save( self,*args,**kwargs ):
        if  self.sub  :
            self.main= self.sub.main

        if self.end :
            self.main=self.end.sub.main
            self.sub=self.end.sub
            
        super(catugry, self).save(*args,**kwargs)






    class Meta:
        verbose_name = "catugry"
        verbose_name_plural = "catsdugry"

    def __str__(self):

        # if self.main is None and self.sub is None:
        #     print("2")
        #     return str(self.name)
        
        # if self.main is not None and self.sub is None:
        #     print("3")
        #     return str(self.main) + " >>>" + str(self.name)
        
        # if self.main is not None and self.sub is not None:
        #     print("4")
        #     print(self.sub.main)

        #     return str(self.main) + " >>>" + str(self.sub) + " >>>" + str(self.name)
        return str(self.name)