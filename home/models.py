from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email=models.EmailField()
    ph=models.CharField(max_length=10)
    ad=models.TextField(max_length=60)

    #def __str__(self):
        #return self.fname+" " +self.lname+" "+self.email+" "+self.ph+" "+self.ad
