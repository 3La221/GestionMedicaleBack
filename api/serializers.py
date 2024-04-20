from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from rest_framework import generics


# Create serializers for each class
class PatientSerializer(ModelSerializer):

    class Meta:
        model = Patient
        fields ='__all__'
        
    def create(self, validated_data):
        user = Patient.objects.create_user(**validated_data)
        return user

class PatientDetailsSerializer(ModelSerializer):
    ordonance_ids = serializers.PrimaryKeyRelatedField(many=True, source='ordonances', read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'carte_id', 'birth_date', 'numero_tel', 'blood_type', 'gender', 'emergency_numbers', 'married', 'maladies', 'ordonance_ids']


class PatientInfoSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','first_name','last_name' ,'carte_id', 'birth_date', 'numero_tel', 'blood_type', 'gender', 'emergency_numbers', 'married', 'maladies']

class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, validated_data):
        user =  Doctor.objects.create_user(**validated_data)
        return user


class DoctorInfoSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields =['id','specialite','first_name','last_name']

    def create(self, validated_data):
        user =  Doctor.objects.create_user(**validated_data)
        return user
class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

    def create(self, validated_data):
        user = Hospital.objects.create_user(**validated_data)
        return user

class MedicamentDetailsSerializer(ModelSerializer):
    class Meta:
        model = MedicamentDetails
        fields = '__all__'
        
class MedicamentSerializer(ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'
        
        
class MaladieSerializer(ModelSerializer):
    class Meta:
        model = Maladie
        fields = '__all__'
        
            
class OrdonanceSerializer(ModelSerializer):
    
    medicaments = MedicamentDetailsSerializer(many=True)  
    
    class Meta:
        model = Ordonance
        fields = ['id', 'date', 'patient', 'doctor', 'maladie', 'medicaments']

    def create(self, validated_data):
        medicaments_data = validated_data.pop('medicaments',[])
        maladies = validated_data.pop('maladie',[])
        patient = validated_data['patient']
        
        ordonance = Ordonance.objects.create(**validated_data)
        
        for medicament_data in medicaments_data:
            MedicamentDetails.objects.create(ordonance = ordonance , **medicament_data)
        
        for maladie in maladies:
            # m = Maladie.objects.get(id=maladie)
            ordonance.maladie.add(maladie)
            patient.maladies.add(maladie)
        
        return ordonance
