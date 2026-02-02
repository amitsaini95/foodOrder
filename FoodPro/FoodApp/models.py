from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
GENDER=(
    ('Male','Male'), 
    ('Female','Female'),
    ('Other','Other'),

)
class Category(models.Model):
    name = models.CharField(max_length=200,null = False, blank = False)
    image = models.CharField(max_length=3000,null = True, blank = True)
    description = models.TextField(max_length=1000,null = False, blank = False)
    
    def __str__(self):
        return self.name
class User(AbstractUser):
    age=models.PositiveIntegerField(null=True)
    gender=models.CharField(choices=GENDER,max_length=10)
    phoneNo=models.IntegerField(null=True)
    address=models.TextField(null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=['email']
    def __str__(self):
        return self.username
class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=400,null = False, blank = False)
    item_description = models.TextField(max_length=1000,null = False, blank = False)
    price = models.FloatField(null = False, blank = False)
    offer_price = models.FloatField(null = False, blank = False)
    item_image = models.CharField(max_length=3000,null = True, blank = True)
    quantity = models.IntegerField(null = False, blank = False)
    underrated_item = models.BooleanField(default=False,help_text="0-show, 1-hidden")
    new_added_item = models.BooleanField(default=False,help_text="0-show, 1-hidden")

    def __str__(self):
        return f'{self.name}'