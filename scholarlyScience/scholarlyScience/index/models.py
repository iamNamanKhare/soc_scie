from django.db import models


class companies(models.Model):
    bgImage = models.TextField()
    companyName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    jobs = models.CharField(max_length=100)
    skill1 = models.CharField(max_length=50)
    skill2 = models.CharField(max_length=50)
    skill3 = models.CharField(max_length=50)
    skill4 = models.CharField(max_length=50)
    skill5 = models.CharField(max_length=50)

class skill(models.Model):
    companie=models.ForeignKey(companies, on_delete=models.CASCADE)
    companies=models.CharField(max_length=50) 
