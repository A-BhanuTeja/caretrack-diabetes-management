from django import forms
from .models import Patient, SugarReading, HealthData
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

# Form 1: Patient Form
class PatientForm(forms.ModelForm):
    """Form for adding/editing patients"""
    
    class Meta:
        model = Patient
        fields = ['name', 'age', 'weight', 'height']
        
        # Custom labels
        labels = {
            'name': 'Full Name',
            'age': 'Age (years)',
            'weight': 'Weight (kg)',
            'height': 'Height (cm)',
        }
        
        # Placeholder text inside input fields
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter full name',
                'class': 'form-control'
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter age',
                'class': 'form-control',
                'min': '1',
                'max': '120'
            }),
            'weight': forms.NumberInput(attrs={
                'placeholder': 'Enter weight in kg',
                'class': 'form-control',
                'step': '0.1'
            }),
            'height': forms.NumberInput(attrs={
                'placeholder': 'Enter height in cm',
                'class': 'form-control',
                'step': '0.1'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('name'),
            Row(
                Column('age', css_class='form-group col-md-4 mb-0'),
                Column('weight', css_class='form-group col-md-4 mb-0'),
                Column('height', css_class='form-group col-md-4 mb-0'),
            ),
            Submit('submit', 'Save Patient', css_class='btn btn-primary mt-3')
        )


# Form 2: Sugar Reading Form
class SugarReadingForm(forms.ModelForm):
    """Form for adding sugar readings"""
    
    class Meta:
        model = SugarReading
        fields = ['reading_date', 'sugar_before_breakfast', 'sugar_after_breakfast', 'notes']
        
        labels = {
            'reading_date': 'Date of Reading',
            'sugar_before_breakfast': 'Fasting Sugar Level (mg/dL)',
            'sugar_after_breakfast': 'Post-Breakfast Sugar Level (mg/dL)',
            'notes': 'Additional Notes (Optional)',
        }
        
        widgets = {
            'reading_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'sugar_before_breakfast': forms.NumberInput(attrs={
                'placeholder': 'e.g., 95',
                'class': 'form-control',
                'min': '0'
            }),
            'sugar_after_breakfast': forms.NumberInput(attrs={
                'placeholder': 'e.g., 130',
                'class': 'form-control',
                'min': '0'
            }),
            'notes': forms.Textarea(attrs={
                'placeholder': 'Any notes about diet, exercise, or how you felt...',
                'class': 'form-control',
                'rows': 3
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Reading', css_class='btn btn-success'))


# Form 3: Health Data Form
class HealthDataForm(forms.ModelForm):
    """Form for adding cholesterol and thyroid data"""
    
    class Meta:
        model = HealthData
        fields = [
            'test_date',
            'cholesterol_total',
            'cholesterol_ldl',
            'cholesterol_hdl',
            'tsh_level'
        ]
        
        labels = {
            'test_date': 'Test Date',
            'cholesterol_total': 'Total Cholesterol (mg/dL)',
            'cholesterol_ldl': 'LDL Cholesterol (mg/dL)',
            'cholesterol_hdl': 'HDL Cholesterol (mg/dL)',
            'tsh_level': 'TSH Level (mIU/L)',
        }
        
        widgets = {
            'test_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'cholesterol_total': forms.NumberInput(attrs={
                'placeholder': 'Optional',
                'class': 'form-control'
            }),
            'cholesterol_ldl': forms.NumberInput(attrs={
                'placeholder': 'Optional',
                'class': 'form-control'
            }),
            'cholesterol_hdl': forms.NumberInput(attrs={
                'placeholder': 'Optional',
                'class': 'form-control'
            }),
            'tsh_level': forms.NumberInput(attrs={
                'placeholder': 'Optional',
                'class': 'form-control',
                'step': '0.01'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Health Data', css_class='btn btn-info'))