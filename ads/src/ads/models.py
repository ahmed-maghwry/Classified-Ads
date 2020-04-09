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




