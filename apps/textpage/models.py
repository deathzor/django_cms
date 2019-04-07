from django.db import models
from django.contrib import admin
# Create your models here.
class textpage(models.Model):
	page = models.CharField(max_length=100,unique=True)
	title = models.CharField(max_length=100)
	html = models.TextField(max_length=30000,default="")
