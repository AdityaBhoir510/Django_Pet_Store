from django.db import models
from django.contrib.auth.models import User
from petsapp.models import Pet

# Create your models here.
class Payment(models.Model):
    payment_id=models.CharField(max_length=150)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    amount_paid=models.CharField(max_length=150)
    status=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.payment_id

class Orders(models.Model):
    status= (('new', 'new'), ('pending' , 'pending' ), ('delivered', 'delivered'), ('cancelled', 'cancelled'))
    states=[
        ('AP', 'Andhra Pradesh'), ('AR', 'Arunchal Pradesh'), ('AS', 'Assam'),
        ( 'BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujrat'), ('HR', 'Haryana'),
        ( 'HP', 'Himanchal Prdesh'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'),
        ( 'MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'),
    ]

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment, on_delete=models.SET_NULL,blank=True, null=True)
    order_number=models.CharField(max_length=20)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100, choices=states, default='MH')
    city=models.CharField(max_length=100)
    total=models.FloatField()
    status=models.CharField(max_length=100, choices=status, default='new')
    ip=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
    
class OrderPet(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    payment=models. ForeignKey(Payment, on_delete=models.SET_NULL,blank=True,null=True)
    pet=models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity=models. IntegerField()
    pet_price=models.FloatField()
    is_orderd=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pet.name