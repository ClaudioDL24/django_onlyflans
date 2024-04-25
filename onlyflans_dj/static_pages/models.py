#from email.policy import default
#from unittest.util import _MAX_LENGTH
import uuid
from django.db import models

# Create your models here.
class Flan(models.Model):
    flan_uuid= models.UUIDField(default=uuid.uuid4, editable=False)
    name= models.CharField(max_length=64)
    description= models.TextField()
    image_url= models.URLField()    
    slug= models.SlugField()
    is_private= models.BooleanField()
    precio = models.DecimalField(max_digits=10, decimal_places=2,  default=0.0)
    receta = models.TextField(default="")  # Campo para almacenar la receta del flan

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

