from django.db import models
from django.core.validators import MinLengthValidator

class Coursecommision(models.Model):
    Uniname=models.CharField(max_length=500,null=True)
    Unimail=models.CharField(max_length=500,null=True)
    Coursename=models.CharField(max_length=500,null=True)
    Coursecurr=models.CharField(max_length=500,null=True)
    Courseamo=models.CharField(max_length=500,null=True)
    Coursecomm=models.CharField(max_length=500,null=True)

    def register(self):
        self.save()