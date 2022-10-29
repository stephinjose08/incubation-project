from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Application(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name="application")
    name=models.CharField(max_length=30,null=True)
    phone=models.CharField(max_length=30,null=True)
    number_of_emp=models.IntegerField(null=True)
    number_of_room=models.IntegerField(null=True)
    number_of_clients=models.IntegerField(null=True)
    company_name=models.CharField(max_length=30,null=True)
    company_Address=models.CharField(max_length=200,null=True)
    company_email=models.CharField(max_length=30,null=True)
    Applied=models.BooleanField(default=True)
    Denied=models.BooleanField(default=False)
    Approved=models.BooleanField(default=False)
    is_alloted=models.BooleanField(default=False)
    alloted_slot=models.IntegerField(null=True)

    def __str__(self):
        return self.company_name

 
class slot(models.Model):
    room_number=models.IntegerField(null=True)
    is_available=models.BooleanField(default=True)
    assigned_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="slot")

    def __str__(self):
        return str(self.room_number)

   