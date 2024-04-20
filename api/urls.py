from django.urls import path,include
from . import views 

urlpatterns = [
    
    #Authentication 
    path("register/", views.register , name="register"),
    path("login/", views.login , name="login"),
    
    #Patient Info
    path("patient/<uuid:pk>/",views.get_patient_details,name="patient-details"),
    
    path("add_ordonance/<uuid:id>/", views.add_ordonance, name="add-ordonance"),
    path("ordonances/<uuid:pk>/" , views.get_patient_ordonances ,name="patient-ordonances" ),    


    path('maladies/', views.MaladieListCreateAPIView.as_view(), name='maladie-list-create'),
    path('maladies/<uuid:pk>/', views.MaladieRetrieveUpdateDestroyAPIView.as_view(), name='maladie-detail'),
    path('medicaments/', views.MedicamentListCreateAPIView.as_view(), name='medicament-list-create'),
    path('medicaments/<uuid:pk>/', views.MedicamentRetrieveUpdateDestroyAPIView.as_view(), name='medicament-detail'),
    
    path('doctor/', views.get_doctors, name='doctor-list-create'),
    
]
