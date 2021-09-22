from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
	categoryname=models.CharField(max_length=150)
	def _str_(self):
		return self.categoryname

# Create your models here.
class Product(models.Model):
	
	name = models.CharField(max_length=150)
	
	price = models.FloatField()
	
	imgup = models.ImageField(null=True)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	def _str_(self):
		return self.name
class Cart(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	


