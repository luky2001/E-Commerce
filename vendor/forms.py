from django import forms
from .models import Recipe,Vendor

class ImageForm(forms.ModelForm):
	class Meta:
		model=Recipe
		fields=['recipe_name','recipe_price','recipe_discription','recipe_image']

class VendorForm(forms.ModelForm):
	class Meta:
		model = Vendor 
		fields=['image','email_id','restaurant_name','address']