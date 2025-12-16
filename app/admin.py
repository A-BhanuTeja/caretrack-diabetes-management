from django.contrib import admin
from .models import Patient, SugarReading, HealthData

# Customize how Patient appears in admin
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Admin interface for Patient model"""
    
    # What columns to show in the list
    list_display = ['name', 'age', 'weight', 'height', 'bmi', 'created_at']
    
    # Add search box
    search_fields = ['name']
    
    # Add filters on the right side
    list_filter = ['age', 'created_at']
    
    # Make BMI read-only (it's auto-calculated)
    readonly_fields = ['bmi', 'created_at', 'updated_at']
    
    # Organize fields in sections
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'age')
        }),
        ('Physical Measurements', {
            'fields': ('weight', 'height', 'bmi')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # This section starts collapsed
        }),
    )


@admin.register(SugarReading)
class SugarReadingAdmin(admin.ModelAdmin):
    """Admin interface for Sugar Reading model"""
    
    list_display = [
        'patient',
        'reading_date',
        'sugar_before_breakfast',
        'sugar_after_breakfast',
        'display_status',
        'created_at'
    ]
    
    search_fields = ['patient__name']  # Search by patient name
    
    list_filter = ['reading_date', 'created_at']
    
    # Order by date (newest first)
    ordering = ['-reading_date']
    
    # Custom method to show status with colors
    def display_status(self, obj):
        """Display status in admin panel"""
        status = obj.get_status()
        return f"Fasting: {status['fasting']}, Post-meal: {status['postmeal']}"
    
    display_status.short_description = 'Status'


@admin.register(HealthData)
class HealthDataAdmin(admin.ModelAdmin):
    """Admin interface for Health Data model"""
    
    list_display = [
        'patient',
        'test_date',
        'cholesterol_total',
        'cholesterol_ldl',
        'cholesterol_hdl',
        'tsh_level'
    ]
    
    search_fields = ['patient__name']
    
    list_filter = ['test_date']
    
    fieldsets = (
        ('Patient Info', {
            'fields': ('patient', 'test_date')
        }),
        ('Cholesterol Levels', {
            'fields': ('cholesterol_total', 'cholesterol_ldl', 'cholesterol_hdl'),
            'description': 'Leave blank if not tested'
        }),
        ('Thyroid Level', {
            'fields': ('tsh_level',),
            'description': 'Leave blank if not tested'
        }),
    )
# Register your models here.
