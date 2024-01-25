from django.db import models
from django.contrib.auth.models import User
from vendor.models import *


class Customer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    customer_image=models.ImageField(upload_to="customer_image")
    customer_email = models.EmailField(max_length=60)
    customer_address = models.TextField()


    def __str__(self):
        return self.customer_email

class CartItem(models.Model):
    product = models.ForeignKey(Recipe, null=True,on_delete=models.CASCADE,)
    user=models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True,default=0)
    def __str__(self):
        return f'{self.product.recipe_name}'
 