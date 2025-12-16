from django.urls import path
from . import views

# App name for namespacing
app_name = 'app'

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # Patient URLs
    path('patient/add/', views.add_patient, name='add_patient'),
    path('patient/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patient/<int:pk>/edit/', views.edit_patient, name='edit_patient'),
    
    # Sugar Reading URLs
    path('reading/add/<int:patient_id>/', views.add_sugar_reading, name='add_sugar_reading'),
    path('reading/<int:pk>/', views.reading_detail, name='reading_detail'),
    
    # Dashboard and History
    path('dashboard/<int:patient_id>/', views.dashboard, name='dashboard'),
    path('history/<int:patient_id>/', views.history, name='history'),
    
    # Health Data URLs
    path('health/add/<int:patient_id>/', views.add_health_data, name='add_health_data'),
]