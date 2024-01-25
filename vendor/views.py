from django.shortcuts import render,redirect,get_object_or_404
from .forms import ImageForm,VendorForm
from django.contrib.auth.forms import User
from .models import Recipe,Vendor
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
	queryset = Recipe.objects.all()
	if request.GET.get('search'):
		queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
	context = {'img':queryset}
	return render(request, 'base.html',context)

def recipe(request):
	vendor = Vendor.objects.get(user=request.user)
	if request.method == "POST":
		form=ImageForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
		obj=Recipe.objects.filter(recipe_name=request.POST['recipe_name']).first()
		obj.vendor=vendor
		obj.save()
		return redirect("/add/")
	form=ImageForm()
	img=Recipe.objects.filter(vendor__user=request.user)
	return render(request,"index.html",{"img":img,"form":form})

def add(request):
	products = Recipe.objects.filter(vendor__user=request.user)
	
	return render(request,'add.html',{"products":products})

def update(request, id):
    recipe= Recipe.objects.get(id=id)
    if request.method == 'POST':
        form = ImageForm(request.POST, instance=recipe)
        if form.is_valid():
        	form.save()
        	return redirect('/add/')
    else:
        form = ImageForm(instance=recipe)
        return render(request,'update.html',{'form': form})

def delete(request,id):
	queryset = Recipe.objects.get(id=id)
	queryset.delete()
	return redirect('/add/')

def register(request):
	if request.method=="POST":
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = User.objects.filter(username=username)
		if user.exists():
			messages.info(request,'username already register')
			return  redirect('/register/')
		user = User.objects.create(
			first_name = first_name,
			last_name = last_name,
			username = username,)
		user.set_password(password)
		user.save()
		messages.info(request,"Account created successfully")
		return redirect('/login/')
	return render(request,'register.html')

def login_page(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')

		if not User.objects.filter(username=username).exists():
			messages.error(request, "Invalid Username")
			return redirect("/login/")
		user =authenticate(username=username,password=password)
		if user is None:
			messages.error(request,"Invalid Password")
			return redirect('/login/')
		else:
			login(request,user)
			return redirect("/dashboard/")
	return render(request,'login.html')

def logout_page(request):
	logout(request)
	return redirect('/')

@login_required(login_url="/login/")
def dashboard(request):
	context = {}
	context["is_vendor"]=False
	obj = Vendor.objects.filter(user=request.user)
	if obj.exists():
		context["is_vendor"]=True

	return render(request,'dashboard.html',context)

def vendor(request):
	if request.method == "POST":
		form=VendorForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			obj=Vendor.objects.filter(email_id=request.POST['email_id']).first()
			obj.user=request.user
			obj.save()
			return redirect("/vendor_details/")
	form=VendorForm()
	#img=Vendor.objects.all()
	return render(request,"vendor.html",{"form":form})

def vendor_details(request):
	vendor = Vendor.objects.get(user=request.user)
	return render(request,'vendor_details.html',{'vendor':vendor})

def update_details(request):
    recipe= Vendor.objects.get(user=request.user)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=recipe)
        if form.is_valid():
        	form.save()
        	return redirect('/vendor_details/')
    else:
        form = VendorForm(instance=recipe)
        return render(request,'vendor_update.html',{'form': form})	