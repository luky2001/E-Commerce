from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
	user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	image=models.ImageField(upload_to="vendor_image")
	email_id=models.EmailField(max_length=60)
	restaurant_name=models.CharField(max_length=100)
	address=models.TextField()
	def __str__(self):
		return self.restaurant_name

class Recipe(models.Model):
	vendor = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE, )
	recipe_name=models.CharField(max_length=100)
	recipe_price=models.IntegerField(null=True)
	recipe_discription=models.TextField(null=True)
	recipe_image=models.ImageField(upload_to='recipe')
	def __str__(self):
		return self.recipe_name

