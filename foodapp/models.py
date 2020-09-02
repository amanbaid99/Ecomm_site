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

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
         return str(self.id)

    # @property
    # def 


class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)


