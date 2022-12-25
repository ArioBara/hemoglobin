from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from groups.models import Group

# Create your models here.


class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50,null=False,blank=False)
    last_name=models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(max_length=255, default=None,unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)
    height = models.CharField(max_length=12, blank=True)
    weight = models.CharField(max_length=12, blank=True)
    disease_history = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, null=False, blank=False)
    BLOOD_CHOICHES = (
        ('gol_A', 'A'),
        ('gol_B', 'B'),
        ('gol_O', 'O'),
        ('gol_AB', 'AB'),)
    blood_group = models.CharField(
        max_length=10, choices=BLOOD_CHOICHES, blank=True)
    GENDER_CHOICHES = (
        ('laki-laki', 'Laki-laki'),
        ('perempuan', 'Perempuan'),
    )
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICHES, blank=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    groups = models.ManyToManyField(Group, blank=True, null=True)

    

    def __str__(self):
        return self.user.username