from django.db import models
from django.contrib import auth


class User(auth.models.User,auth.models.PermissionsMixin,models.Model):

    
    def __str__(self):
        return "@{}".format(self.username)

class Business(models.Model):
    bname=models.CharField(max_length=200,null=False)
    specialities=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=False)
    # image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.bname

    @property
    def imageURL(self):

        try:
            url=self.image.url
        except:
            url= ''
        return url




