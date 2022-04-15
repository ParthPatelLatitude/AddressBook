from django.db import models
import uuid
# Create your models here.

class utl_status(models.Model):
    value = models.CharField(max_length=60,blank=True)

    created_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value


class UserSignup(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,unique=True)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=150,blank=True,null=True)

    created_date_time = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(utl_status,on_delete=models.CASCADE,default = 1)


    def __str__(self):
        return self.email_id


class UserProfile(models.Model):
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    phone_number = models.IntegerField(blank=True,null=True)
    address = models.TextField(max_length=250,blank=True,null=True)

    created_date_time = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(utl_status,on_delete=models.CASCADE,default = 1)

    def __str__(self):
        return self.first_name



class SqlLogin(models.Model):
    action = models.CharField(max_length=50,blank=True,null=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     abstract = True
    # def __str__(self):
    #     return self.action