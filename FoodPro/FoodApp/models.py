from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
GENDER=(
    ('Male','Male'), 
    ('Female','Female'),
    ('Other','Other'),

)
class User(AbstractUser):
    age=models.PositiveIntegerField(null=True)
    gender=models.CharField(choices=GENDER,max_length=10)
    phoneNo=models.IntegerField(null=True)
    address=models.TextField(null=True)

    def __str__(self):
        return self.username