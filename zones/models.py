#from django.db import models
from django.contrib.gis.db import models
from django.core.validators import RegexValidator

class Supplier(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Zone(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, related_name='zones', on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, related_name='zones')
    
    zone = models.PolygonField()

    def __str__(self):
        return self.name

