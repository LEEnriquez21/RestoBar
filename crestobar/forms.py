from django import forms
from django.forms import ModelForm
from .models import Reservation, Table, Product
from django.contrib.auth.forms import AuthenticationForm

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('full_name', 'product_name', 'attendees', 'phone', 'email', 'reservation_expected', 'description','status')
        labels = {
            'full_name': 'Enter Full name:',
            'product_name': 'Expected Order',
            'attendees': 'How Many are you?',
            'phone': 'Contact Number',
            'email': 'Email',
            'reservation_expected': 'When Will you be Reserved  MM/DD/YYYY HH:MM:SS',
            'description': 'Any More addition',
            'status': 'Reservation Status',

 
        }
        widgets ={
            'full_name': forms.TextInput(attrs={'class':'form-control'}),
            'product_name':forms.Select(attrs={'class':'form-select'}),
            'attendees':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'reservation_expected':forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'MM/DD/YYYY HH:MM:SS'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-select', 'placeholder':'pending','disabled':'true'}),

        }

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ('table_name', 'avail_seat', 'table_number')
        labels = {
            'table_name': 'Table Name:',
            'avail_seat': 'Seating Capacity',
            'table_number': 'Identification Number',
        }
        widgets ={
            'table_name': forms.TextInput(attrs={'class':'form-control'}),
            'avail_seat':forms.NumberInput(attrs={'class':'form-control'}),
            'table_number':forms.NumberInput(attrs={'class':'form-control'}),
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'price', 'description', 'image')
        labels = {
            'product_name': 'Product Name:',
            'price': 'Price',
            'description': 'Description of the Product',
            'image': 'Insert Image',

        }
        widgets ={
            'product_name': forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }

class UpdateReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('full_name', 'product_name', 'attendees', 'phone', 'email', 'reservation_expected', 'table','description','status')
        labels = {
            'full_name': 'Enter Full name:',
            'product_name': 'Expected Order',
            'table': 'Designate Table',
            'attendees': 'How Many are you?',
            'phone': 'Contact Number',
            'email': 'Email',
            'reservation_expected': 'When Will you be Reserved  MM/DD/YYYY HH:MM:SS',
            'description': 'Any More addition',
            'status': 'Reservation Status',

 
        }
        widgets ={
            'full_name': forms.TextInput(attrs={'class':'form-control'}),
            'product_name':forms.Select(attrs={'class':'form-select'}),
            'table':forms.Select(attrs={'class':'form-select'}),
            'attendees':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'reservation_expected':forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'MM/DD/YYYY HH:MM:SS'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-select'}),

        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
        


