from django.db import models
from django.db.models import Q

from django.db.models.signals import pre_save
from petsapp.utils import unique_slug_generator

# Create your models here.
class PetsQuerySet(models.QuerySet):
    def dog_list(self):
        return self.filter(animal_type='D')

    def cat_list(self):
        return self.filter(animal_type='C')
    
    def search(self, query):
        print (query)
        lookups = (Q(name__icontains=query) | Q(animal_type__icontains=query) | Q(breed__icontains=query) |Q(age__icontains=query))
        return self.filter(lookups)

        
class CustomManager(models.Manager) :
    def get_pets_price_range(self, r1, r2):
        return super().get_queryset().filter(price__range=(r1, r2))  
    
    def get_queryset(self):
        return PetsQuerySet(self.model, using=self._db)

    def dog_list(self):
        return self.get_queryset().dog_list()

    def cat_list(self):
        return self.get_queryset().cat_list() 
    
    def search(self,query):
        print(query)
        return self.get_queryset().search(query)
    
    def expensive_pets_view(self):
        return super().get_queryset().filter(Q(price__gt=5000))      
        
class Pet(models.Model):
    gender = [
        ("male","male"),
        ("female","female")
    ]
    type = [
        ("D","Dog"),
        ("C","Cat")
    ]
    image = models.ImageField(upload_to="media")
    name = models.CharField(max_length=100)
    price = models.FloatField(default="10")
    animal_type = models.CharField(max_length=30,choices=type)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50,choices=gender)
    description = models.CharField(max_length=255)
    
    objects = models.Manager()
    pets = CustomManager()
    pet = PetsQuerySet.as_manager()
    slug=models.SlugField(max_length=30,null = True)
    
    class Meta:
        db_table = "Pet"

def pets_pre_save_receiver(sender, instance, *args, **kwargs):
    print("pets_pre_save_receiver")
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        print(instance.slug)
        
pre_save.connect(pets_pre_save_receiver,sender=Pet)