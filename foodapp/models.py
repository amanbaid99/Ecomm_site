from django.db import models
from django.contrib import auth
from django.conf import settings



class User(auth.models.User,auth.models.PermissionsMixin,models.Model):
   
    def __str__(self):
        return "@{}".format(self.username)
    

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    digital=models.BooleanField(default=False,null=False,blank=False)
    image = models.ImageField(null=True,blank=True)
    description=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name

    
    @property
    def imageURL(self):

        try:
            url=self.image.url
        except:
            url= ''
        return url


