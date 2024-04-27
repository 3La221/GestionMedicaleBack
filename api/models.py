from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import uuid
from . managers import ProfileManager
from .enums import *


class Profile(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    
    USERNAME_FIELD = "id"
    
    PASSWORD_FIELD = 'password'

    REQUIRED_FIELDS = []
    
    objects = ProfileManager()
    
    

class Patient(Profile):
    carte_id = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField(null = True)
    numero_tel = models.CharField(max_length=20, blank=True, null=True)
    blood_type = models.CharField(max_length=3, choices=[(tag.value, tag.name) for tag in BloodType],null=True , blank = True)
    gender = models.CharField(max_length=10, choices=[(tag.value, tag.name) for tag in Gender],null=True , blank = True)
    emergency_number = models.CharField(max_length=20, blank=True, null=True)
    married = models.BooleanField(default=False)  
    maladies = models.ManyToManyField("Maladie",blank=True)
    REQUIRED_FIELDS = ["carte_id"]

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        
    def __str__(self) -> str:
        return  f'{self.first_name} {self.last_name}'

class Doctor(Profile):
    carte_id = models.CharField(max_length=255, unique=True)
    specialite = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in Specialite] , default = Specialite.AUTRE)
    hospitals = models.ManyToManyField("Hospital",related_name="doctors" , blank=True)
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        
    def __str__(self) -> str:
        return  f'Dr.{self.first_name} {self.last_name}'
    
class Hospital(Profile):
    name = models.CharField(max_length=100, blank=True, null=True)
    hospital_address = models.CharField(max_length=100, blank=True, null=True)
    hospital_number  = models.CharField(max_length=10, blank=True, null=True)
    
    
    class Meta:
        verbose_name = "Hosptial"
        verbose_name_plural = "Hospitals"
        
    def __str__(self) -> str:
        return  f'{self.name} Hospital'

class Labo(Profile):
    name = models.CharField(max_length=100, blank=True, null=True)
    labo_address = models.CharField(max_length=100, blank=True, null=True)
    labo_number  = models.CharField(max_length=10, blank=True, null=True)
    
    
    class Meta:
        verbose_name = "Labo"
        verbose_name_plural = "Labos"
        
    def __str__(self) -> str:
        return  f'{self.name} Labo'
    
class Ordonance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(default=timezone.now)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name ="ordonances")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name ="doctors")
    maladie = models.ManyToManyField("Maladie",related_name ="maladies")
    
    
class Maladie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,blank=True,null= True)
    isChronic = models.BooleanField(default=False)
    maladie_type = models.CharField(max_length=80,choices=[(tag.name,tag.value) for tag in TypeMaladie])

    def __str__(self) -> str:
        return self.name

class Medicament(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)    
    
class MedicamentDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ratio = models.IntegerField(default=1)
    duree = models.IntegerField(default=7)
    notes = models.TextField(blank=True, null = True)
    isChronic = models.BooleanField(default=False)
    medicament = models.ForeignKey(Medicament,null=True,blank=True , on_delete=models.CASCADE)
    ordonance = models.ForeignKey(Ordonance , on_delete = models.CASCADE , null = True , blank =True,related_name="medicaments")
    


    
