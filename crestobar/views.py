from django.shortcuts import render, redirect
from .models import *
from .forms import ReservationForm, TableForm, ProductForm, UpdateReservationForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.


def home_page(request):
	products = Product.objects.all()

	context = {
		'products':products
	}

	return render(request,  'pages/home.html', context)

def reservation_page(request):
	form = ReservationForm()
	if request.method == 'POST':
		form = ReservationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('Homepage')
	context = {
		'form':form
	}
	return render(request,  'pages/reservation.html', context)

def admin_page(request):
	products = Product.objects.all()
	reservations = Reservation.objects.all()
	reservation_status = Reservation.objects.all()
	tables = Table.objects.all()

	total_table = tables.count()
	total_product = products.count()

	pending = reservation_status.filter(status='P').count()
	accepted = reservation_status.filter(status='A').count()
	denied = reservation_status.filter(status='D').count()

	context = {
		'products':products,
		'tables':tables,
		'reservations':reservations,
		'pending':pending,
		'accepted':accepted,
		'denied':denied,
		'total_product':total_product,
		'total_table':total_table

	}
	return render(request,  'pages/admin.html', context)

def product_page(request):
	products = Product.objects.all()
	context = {
		'products':products,
	}

	return render(request,  'pages/product.html', context)

def table_page(request):
	tables = Table.objects.all()
	context = {
		'tables':tables,
	}
	return render(request,  'pages/table.html', context)

def r_form_page(request):
	reservations = Reservation.objects.all()
	context = {
		'reservations':reservations,
	}
	return render(request,  'pages/r_form.html', context)

def T_add_page(request):
	form = TableForm()
	if request.method == 'POST':
		form = TableForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('table')
	context = {
		'form':form
	}
	return render(request,  'pages/T_add.html', context)

def p_add_page(request):
	form = ProductForm()
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('product')
	context = {
		'form':form
	}
	return render(request,  'pages/product_add.html', context)

def update_reservation(request, reservation_id):
	reservation = Reservation.objects.get(pk=reservation_id)
	form = UpdateReservationForm(request.POST or None, instance=reservation)
	if form.is_valid():
		form.save()
		return redirect('r_form')
	
	return render(request, 'pages/update_reservation.html', {'reservation':reservation,'form':form})

def update_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	form = ProductForm(request.POST or None, request.FILES or None, instance=product)
	if form.is_valid():
		form.save()
		return redirect('product')
	
	return render(request, 'pages/update_product.html', {'product':product,'form':form})

def update_table(request, table_id):
	table = Table.objects.get(pk=table_id)
	form = TableForm(request.POST or None, instance=table)
	if form.is_valid():
		form.save()
		return redirect('table')
	
	return render(request, 'pages/update_table.html', {'table':table,'form':form})


def deleteTable(request,id):
	dele = Table.objects.get(id=id)
	dele.delete()
	return redirect('table')

def deleteReservation(request,id):
	dele = Reservation.objects.get(id=id)
	dele.delete()
	return redirect('r_form')

def deleteProduct(request,id):
	dele = Product.objects.get(id=id)
	dele.delete()
	return redirect('product')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin')
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'form': form})
