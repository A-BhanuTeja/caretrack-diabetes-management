from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Patient, SugarReading, HealthData
from .forms import PatientForm, SugarReadingForm, HealthDataForm
import plotly.graph_objects as go
from datetime import datetime, timedelta
from .diet_plans import get_detailed_diet_plan

# View 1: Home Page
def home(request):
    """Display home page with list of all patients"""
    patients = Patient.objects.all()
    
    context = {
        'patients': patients,
    }
    
    return render(request, 'app/home.html', context)


# View 2: Add Patient
def add_patient(request):
    """Add a new patient"""
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, f'Patient {patient.name} added successfully!')
            return redirect('app:patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    
    context = {
        'form': form,
        'title': 'Add New Patient'
    }
    
    return render(request, 'app/patient_form.html', context)


# View 3: Patient Detail
def patient_detail(request, pk):
    """Display detailed information about a patient"""
    patient = get_object_or_404(Patient, pk=pk)
    
    # Get latest sugar reading
    latest_reading = patient.sugar_readings.first()
    
    # Get recent readings (last 7 days)
    recent_readings = patient.sugar_readings.all()[:7]
    
    # Get health data
    health_data = patient.health_data.first()
    
    context = {
        'patient': patient,
        'latest_reading': latest_reading,
        'recent_readings': recent_readings,
        'health_data': health_data,
    }
    
    return render(request, 'app/patient_detail.html', context)


# View 4: Edit Patient
def edit_patient(request, pk):
    """Edit existing patient information"""
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, f'Patient {patient.name} updated successfully!')
            return redirect('app:patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    
    context = {
        'form': form,
        'title': f'Edit {patient.name}',
        'patient': patient,
    }
    
    return render(request, 'app/patient_form.html', context)


# View 5: Add Sugar Reading
def add_sugar_reading(request, patient_id):
    """Add a new sugar reading for a patient"""
    patient = get_object_or_404(Patient, pk=patient_id)
    
    if request.method == 'POST':
        form = SugarReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.patient = patient
            reading.save()
            messages.success(request, 'Sugar reading added successfully!')
            return redirect('app:patient_detail', pk=patient.pk)
    else:
        form = SugarReadingForm()
    
    context = {
        'form': form,
        'patient': patient,
        'title': f'Add Sugar Reading for {patient.name}'
    }
    
    return render(request, 'app/reading_form.html', context)


# View 6: Reading Detail
def reading_detail(request, pk):
    """Display detailed information about a specific reading"""
    reading = get_object_or_404(SugarReading, pk=pk)
    status = reading.get_status()
    patient = reading.patient
    
    # Get detailed diet plan
    diet_plan = get_detailed_diet_plan(
        status=status,
        patient_age=patient.age,
        bmi=float(patient.bmi) if patient.bmi else 25.0
    )
    
    context = {
        'reading': reading,
        'status': status,
        'diet_plan': diet_plan,  # Changed from meal_suggestions
        'patient': patient,
    }
    
    return render(request, 'app/reading_detail.html', context)


# View 7: Dashboard with Graphs
def dashboard(request, patient_id):
    """Display patient dashboard with graphs"""
    patient = get_object_or_404(Patient, pk=patient_id)
    
    # Get all readings for this patient
    readings = patient.sugar_readings.all()[:30]  # Last 30 readings
    
    # Create graph if there are readings
    graph_html = None
    if readings:
        graph_html = create_sugar_graph(readings)
    
    # Calculate statistics
    if readings:
        fasting_values = [r.sugar_before_breakfast for r in readings]
        postmeal_values = [r.sugar_after_breakfast for r in readings]
        
        stats = {
            'avg_fasting': sum(fasting_values) / len(fasting_values),
            'avg_postmeal': sum(postmeal_values) / len(postmeal_values),
            'min_fasting': min(fasting_values),
            'max_fasting': max(fasting_values),
            'min_postmeal': min(postmeal_values),
            'max_postmeal': max(postmeal_values),
        }
    else:
        stats = None
    
    context = {
        'patient': patient,
        'graph_html': graph_html,
        'stats': stats,
        'readings_count': readings.count(),
    }
    
    return render(request, 'app/dashboard.html', context)


# View 8: History Page
def history(request, patient_id):
    """Display complete history of readings"""
    patient = get_object_or_404(Patient, pk=patient_id)
    readings = patient.sugar_readings.all()
    
    context = {
        'patient': patient,
        'readings': readings,
    }
    
    return render(request, 'app/history.html', context)


# View 9: Add Health Data
def add_health_data(request, patient_id):
    """Add cholesterol and thyroid data"""
    patient = get_object_or_404(Patient, pk=patient_id)
    
    if request.method == 'POST':
        form = HealthDataForm(request.POST)
        if form.is_valid():
            health_data = form.save(commit=False)
            health_data.patient = patient
            health_data.save()
            messages.success(request, 'Health data added successfully!')
            return redirect('app:patient_detail', pk=patient.pk)
    else:
        form = HealthDataForm()
    
    context = {
        'form': form,
        'patient': patient,
        'title': f'Add Health Data for {patient.name}'
    }
    
    return render(request, 'app/health_data_form.html', context)


# Helper Function: Create Graph using Plotly
def create_sugar_graph(readings):
    """Create an interactive line graph of sugar levels"""
    
    # Extract data from readings (reverse to show oldest to newest)
    dates = [r.reading_date for r in reversed(readings)]
    fasting = [r.sugar_before_breakfast for r in reversed(readings)]
    postmeal = [r.sugar_after_breakfast for r in reversed(readings)]
    
    # Create figure
    fig = go.Figure()
    
    # Add fasting sugar line
    fig.add_trace(go.Scatter(
        x=dates,
        y=fasting,
        mode='lines+markers',
        name='Fasting Sugar',
        line=dict(color='blue', width=2),
        marker=dict(size=8)
    ))
    
    # Add post-meal sugar line
    fig.add_trace(go.Scatter(
        x=dates,
        y=postmeal,
        mode='lines+markers',
        name='Post-Meal Sugar',
        line=dict(color='red', width=2),
        marker=dict(size=8)
    ))
    
    # Add reference lines for normal ranges
    fig.add_hline(y=100, line_dash="dash", line_color="green", 
                  annotation_text="Normal Fasting (100)")
    fig.add_hline(y=140, line_dash="dash", line_color="orange",
                  annotation_text="Normal Post-Meal (140)")
    
    # Update layout
    fig.update_layout(
        title='Sugar Level Trends',
        xaxis_title='Date',
        yaxis_title='Sugar Level (mg/dL)',
        hovermode='x unified',
        template='plotly_white',
        height=500,
    )
    
    # Convert to HTML
    return fig.to_html(full_html=False, include_plotlyjs='cdn')


# Helper Function: Get Meal Suggestions
def get_meal_suggestions(status):
    """Provide meal suggestions based on sugar status"""
    
    suggestions = {
        'foods_to_eat': [],
        'foods_to_avoid': [],
        'tips': []
    }
    
    # If fasting sugar is high
    if status['fasting'] == 'High':
        suggestions['foods_to_eat'] = [
            'Leafy green vegetables (spinach, kale)',
            'Whole grains (oats, brown rice)',
            'Lean proteins (chicken, fish)',
            'Nuts and seeds (almonds, walnuts)',
            'Legumes (lentils, chickpeas)',
        ]
        suggestions['foods_to_avoid'] = [
            'White bread and refined flour',
            'Sugary drinks and sodas',
            'Sweets and desserts',
            'Fried foods',
            'Processed snacks',
        ]
        suggestions['tips'] = [
            'Eat smaller, frequent meals',
            'Exercise for 30 minutes daily',
            'Stay hydrated with water',
            'Get adequate sleep (7-8 hours)',
        ]
    
    # If fasting sugar is low
    elif status['fasting'] == 'Low':
        suggestions['foods_to_eat'] = [
            'Fresh fruits (banana, apple)',
            'Whole grain toast with peanut butter',
            'Greek yogurt',
            'Small handful of nuts',
            'Smoothie with fruits',
        ]
        suggestions['foods_to_avoid'] = [
            'Skipping meals',
            'Excessive caffeine',
            'Alcohol on empty stomach',
        ]
        suggestions['tips'] = [
            'Eat regular meals - don\'t skip breakfast',
            'Carry healthy snacks',
            'Monitor symptoms of low blood sugar',
        ]
    
    # If post-meal sugar is high
    if status['postmeal'] == 'High':
        suggestions['tips'].append('Walk for 10-15 minutes after meals')
        suggestions['tips'].append('Reduce portion sizes')
        suggestions['tips'].append('Avoid sugary desserts after meals')
    
    # If both are normal
    if status['fasting'] == 'Normal' and status['postmeal'] == 'Normal':
        suggestions['foods_to_eat'] = [
            'Continue balanced diet with vegetables',
            'Include lean proteins',
            'Eat whole grains',
            'Stay hydrated',
        ]
        suggestions['tips'] = [
            'Maintain your current healthy lifestyle!',
            'Continue regular exercise',
            'Keep monitoring your levels',
        ]
    
    return suggestions