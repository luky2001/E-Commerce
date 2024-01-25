from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields=['customer_email','customer_address','customer_image']
