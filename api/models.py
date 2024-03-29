from django.db import models

class Role(models.Model):
    role_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
       return self.name

class Employee(models.Model):
    username = models.CharField(max_length=255,primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
       return self.name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12,unique=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class CustomerInteraction(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    visiting_date = models.DateField()
    prospect_status = models.CharField(max_length=255)
    outcome = models.CharField(max_length=255)

class EmployeeTravelAllowance(models.Model):
    starting_location = models.CharField(max_length=255)
    ending_location = models.CharField(max_length=255)
    starting_kilometer = models.IntegerField(null=True, blank=True)
    ending_kilometer = models.IntegerField(null=True, blank=True)
    amount = models.BigIntegerField()
    created_at = models.DateTimeField()
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, related_name="travel_allowances")
