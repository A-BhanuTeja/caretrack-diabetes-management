from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Model 1: Patient Information
class Patient(models.Model):
    """Stores basic patient information"""
    
    # CharField = Text field with max length
    name = models.CharField(max_length=100, help_text="Patient's full name")
    
    # PositiveIntegerField = Only positive numbers (age can't be negative!)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)],
        help_text="Age in years"
    )
    
    # DecimalField = Numbers with decimals (for weight/height)
    weight = models.DecimalField(
        max_digits=5,      # Total digits (e.g., 150.5 = 4 digits)
        decimal_places=2,  # Digits after decimal
        help_text="Weight in kg"
    )
    
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Height in cm"
    )
    
    # Automatically calculated BMI
    bmi = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,  # Can be empty initially
        null=True,   # Can be NULL in database
        help_text="Body Mass Index (calculated automatically)"
    )
    
    # DateTimeField = Stores date and time
    created_at = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated_at = models.DateTimeField(auto_now=True)      # Updates every time we save
    
    def calculate_bmi(self):
        """Calculate BMI: weight(kg) / (height(m))^2"""
        if self.weight and self.height:
            height_in_meters = self.height / 100  # Convert cm to meters
            self.bmi = self.weight / (height_in_meters ** 2)
    
    def save(self, *args, **kwargs):
        """Override save to calculate BMI before saving"""
        self.calculate_bmi()
        super().save(*args, **kwargs)
    
    def __str__(self):
        """What shows when we print this object"""
        return f"{self.name} (Age: {self.age})"
    
    class Meta:
        ordering = ['-created_at']  # Newest first


# Model 2: Sugar Readings
class SugarReading(models.Model):
    """Stores daily sugar level readings"""
    
    # ForeignKey = Links to Patient (many readings belong to one patient)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,  # If patient deleted, delete all their readings
        related_name='sugar_readings'
    )
    
    # Date of reading
    reading_date = models.DateField(default=timezone.now)
    
    # Sugar levels (mg/dL)
    sugar_before_breakfast = models.PositiveIntegerField(
        help_text="Fasting sugar level (mg/dL)"
    )
    
    sugar_after_breakfast = models.PositiveIntegerField(
        help_text="Post-meal sugar level (mg/dL)"
    )
    
    # Optional fields
    notes = models.TextField(blank=True, help_text="Any additional notes")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_status(self):
        """Determine if sugar levels are normal, high, or low"""
        # Fasting (before breakfast) normal range: 70-100 mg/dL
        # Post-meal (after breakfast) normal range: Less than 140 mg/dL
        
        if self.sugar_before_breakfast < 70:
            fasting_status = "Low"
        elif 70 <= self.sugar_before_breakfast <= 100:
            fasting_status = "Normal"
        else:
            fasting_status = "High"
        
        if self.sugar_after_breakfast < 140:
            postmeal_status = "Normal"
        else:
            postmeal_status = "High"
        
        return {
            'fasting': fasting_status,
            'postmeal': postmeal_status
        }
    
    def __str__(self):
        return f"{self.patient.name} - {self.reading_date}"
    
    class Meta:
        ordering = ['-reading_date']  # Most recent first
        unique_together = ['patient', 'reading_date']  # One reading per day per patient


# Model 3: Additional Health Data (Optional)
class HealthData(models.Model):
    """Stores cholesterol and thyroid data"""
    
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='health_data'
    )
    
    test_date = models.DateField(default=timezone.now)
    
    # Cholesterol levels (optional)
    cholesterol_total = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Total cholesterol (mg/dL)"
    )
    
    cholesterol_ldl = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="LDL (bad) cholesterol (mg/dL)"
    )
    
    cholesterol_hdl = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="HDL (good) cholesterol (mg/dL)"
    )
    
    # Thyroid levels (optional)
    tsh_level = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="TSH level (mIU/L)"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient.name} - Health Data {self.test_date}"
    
    class Meta:
        ordering = ['-test_date']
# Create your models here.
