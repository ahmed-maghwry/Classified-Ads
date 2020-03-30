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


    class Meta:
        ordering = ['-view']
    def __str__(self):
        return self.title
