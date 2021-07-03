from typing import Tuple
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
         return self.name


class Models(models.Model):
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='models/img')

    def __str__(self):
         return self.name


class ModelPart(models.Model):
    model_name = models.ForeignKey(Models, on_delete=models.CASCADE)
    part_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
         return self.part_name


class Parts(models.Model):
    part_name = models.ForeignKey(ModelPart, on_delete=models.CASCADE)

    def __str__(self):
         return self.part_name.part_name


class Companies(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
         return self.name


class Invoice(models.Model):
    company_name = models.ForeignKey(Companies, on_delete=models.CASCADE)
    serial_no = models.IntegerField(unique=True)
    date = models.DateField(blank=True, null=True)
    total_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
         return f"No is {self.serial_no} {self.company_name.name}"


class Inventory(models.Model):
    part_name = models.ForeignKey(Parts, on_delete=models.CASCADE)
    initial_qty = models.IntegerField(default=1)
    initial_price = models.IntegerField(default=0)
    current_qty = models.IntegerField(default=1)
    current_price = models.IntegerField(default=0)
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self):
         return self.part_name.part_name.part_name


class ClientCompany(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
         return self.name


class Client(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    primary_phone = models.CharField(
        default="+1", max_length=12, blank=True, null=True)
    secondary_phone = models.CharField(
        default="+1", max_length=12, blank=True, null=True)

    def __str__(self):
         return self.username.username


class Labors(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	price = models.DecimalField(max_digits=15, decimal_places=2)

    # def __str__(self):
    #     return self.name           
    
class Repairs(models.Model):
    client_name = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    model_name = models.ForeignKey(Models, on_delete=models.CASCADE)
    battery_sn = models.IntegerField(default=50, unique=True)
    accessories = models.CharField(max_length=150, blank=True, null=True)
    security_code = models.IntegerField(default=50, unique=True)
    initial_state = models.CharField(max_length=150, blank=True, null=True)
    client_defects = models.TextField()
    service_defects = models.TextField()
    repair_description = models.TextField()
    service_notes = models.CharField(max_length=150, blank=True, null=True)
    
    total = models.ForeignKey(Labors, on_delete=models.CASCADE)

    discount = models.DecimalField(max_digits=15, decimal_places=2)
    finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
         return self.model_name.name

class RepairLabor(models.Model):
    labor_name = models.ForeignKey(Labors, on_delete=models.CASCADE)
    repair_id = models.ForeignKey(Repairs, on_delete=models.CASCADE)

    def __str__(self):
         return self.labor_name.name
  
class Status(models.Model):
    status = models.BooleanField(default=False)
    
    # def __str__(self):
    #      if self.status == True:
    #          return f"Completed{self.status}"
    #      else:
    #         return f"Completed{self.status}"
  
class RepairStatus(models.Model):
	repair_id = models.ForeignKey(Repairs, on_delete=models.CASCADE)
	status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # def __str__(self):
    #      return self.repair_id.client_defects
    
  
class Operations(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)

    # def __str__(self):
    #      return self.name

  
class InventoryOperations(models.Model):
	inventory_name = models.ForeignKey(Inventory, on_delete=models.CASCADE)
	operations_name = models.ForeignKey(Operations, on_delete=models.CASCADE)
	explanation = models.TextField()
	price = models.DecimalField(max_digits=15, decimal_places=2)
	qty = models.IntegerField(default=1)
	repair_id = models.ForeignKey(Repairs, on_delete=models.CASCADE)
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #      return self.operations_name.name

  
class Messages(models.Model):
	repair_id = models.ForeignKey(Repairs, on_delete=models.CASCADE)
	types = models.CharField(max_length=50)
	template = models.TextField()
	delivered = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    # def __str__(self):
    #     return self.template
    


