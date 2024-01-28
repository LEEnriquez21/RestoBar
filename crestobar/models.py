from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='Product/', blank=True,null=True)
    
    def __str__(self):
        return self.product_name

class Table(models.Model):
    table_name = models.CharField(max_length=100, null=True)
    avail_seat = models.IntegerField()
    table_number = models.IntegerField()
    def __str__(self):
        return f'{self.table_name} {self.table_number}'

class Reservation(models.Model):
    STATUS = (
        ('P','Pending'),
        ('A','Accepted'),
        ('D','Denied')
    )
    full_name = models.CharField(max_length=250, null=True)
    product_name = models.ForeignKey(Product,null=True, blank=True , on_delete= models.SET_NULL)
    attendees = models.IntegerField(default=1)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=250, blank=True)
    datecreated = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True,  blank = True, default = 'P', choices=STATUS)
    reservation_expected = models.DateTimeField()
    description = models.CharField(max_length=250, blank=True, null=True)
    table = models.ForeignKey(Table, null=True, blank = True, on_delete= models.SET_NULL)
    def __str__(self):
          return f'{self.full_name} {self.datecreated}'