from django.db import models
from petsapp.models import Pet
from django.contrib.auth.models import User 

# Create your models here.
class Cart(models.Model) :
    cart_id=models.CharField(max_length=250, blank=True)
    pet=models.ForeignKey(Pet, on_delete = models. CASCADE)
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    quantity=models.IntegerField(default = 1)
    totalprice=models.FloatField(default = 0.00)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        db_table='cart'