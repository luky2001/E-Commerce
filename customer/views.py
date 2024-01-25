from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import User
from django.contrib import messages
from .forms import CustomerForm
from .models import Customer,CartItem
from vendor.models import *
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
import json

def homes(request):
	return render(request,'home.html')

def customer_register(request):
	if request.method=="POST":
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = User.objects.filter(username=username)
		if user.exists():
			messages.info(request,'username already register')
			return  redirect('/customer/customer_register/')
		user = User.objects.create(
			first_name = first_name,
			last_name = last_name,
			username = username,)
		user.set_password(password)
		user.save()
		messages.info(request,"Account created successfully")
		return redirect('/customer_login/')
	return render(request,'customer_register.html')

def customer_login(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')

		if not User.objects.filter(username=username).exists():
			messages.error(request, "Invalid Username")
			return redirect("/customer/customer_login/")
		user =authenticate(username=username,password=password)
		if user is None:
			messages.error(request,"Invalid Password")
			return redirect('/customer/customer_login/')
		else:
			login(request,user)
			return redirect("/customer/customer_dashboard/")
	return render(request,'customer_login.html')

def customer_logout(request):
	logout(request)
	return redirect('/')

def customer_profile(request):
	if request.method == "POST":
		form=CustomerForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			obj=Customer.objects.filter(customer_email=request.POST['customer_email']).first()
			obj.user=request.user
			obj.save()
			return redirect("/customer/customer_details/")
	form=CustomerForm()
	#img=Vendor.objects.all()
	return render(request,"customer_profile.html",{"form":form})
	
def customer_details(request):
	user = Customer.objects.get(user=request.user)
	return render(request,'customer_details.html',{'user':user})
def customer_update(request):
    recipe= Customer.objects.get(user=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=recipe)
        if form.is_valid():
        	form.save()
        	return redirect('/customer/customer_details/')
    else:
        form = CustomerForm(instance=recipe)
        return render(request,'customer_update.html',{'form': form})	
@login_required(login_url="/login/")
def customer_dashboard(request):
	context = {}
	context["is_vendor"]=False
	obj = Customer.objects.filter(user=request.user)
	if obj.exists():
		context["is_vendor"]=True
	queryset = Recipe.objects.all()
	if request.GET.get('search'):
		queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
	context['img']=queryset
	return render(request,'customer_dashboard.html',context)
	
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.recipe_price * item.quantity for item in cart_items)
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def addcart(request, product_id):
    product = Recipe.objects.get(id=product_id)
    cart_obj=CartItem.objects.filter(user=request.user,product=product)
    if not cart_obj.exists():
    	obj=CartItem(product=product,user=request.user,quantity=1)
    	obj.save()
    else:
    	cart_obj=cart_obj.first()
    	cart_obj.quantity=cart_obj.quantity+1
    	cart_obj.save()
    return redirect('/customer/cart/')
 
def remove_cart(request,id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect('/customer/cart/')
 