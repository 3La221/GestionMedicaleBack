from enum import Enum





class TypeMaladie(Enum):
    CARDIOVASCULAIRE = "Maladie cardiovasculaire"
    RESPIRATOIRE = "Maladie respiratoire"
    INFECTIEUSE = "Maladie infectieuse"
    AUTOIMMUNE = "Maladie auto-immune"
    MENTALE = "Maladie mentale"
    GENETIQUE = "Maladie génétique"
    CANCER = "Cancer"
    METABOLIQUE = "Trouble métabolique"
    NEUROLOGIQUE = "Trouble neurologique"
    AUTRE = "Autre"

class BloodType(Enum):
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    B_POSITIVE = 'B+'
    B_NEGATIVE = 'B-'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'

class Specialite(Enum):
    CARDIOLOGIE = 'Cardiologie'
    DERMATOLOGIE = 'Dermatologie'
    GASTRO_ENTEROLOGIE = 'Gastro-entérologie'
    NEUROLOGIE = 'Neurologie'
    PEDIATRIE = 'Pédiatrie'
    PSYCHIATRIE = 'Psychiatrie'
    RADIOLOGIE = 'Radiologie'
    CHIRURGIE = 'Chirurgie'
    AUTRE = 'Autre'
