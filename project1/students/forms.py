from django import forms
from .models import Student, Diagnostic

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'birth_date', 'gender', 'current_school_name', 'current_school_grade', 'name_en']
        widgets = {
            'birth_date': forms.DateInput(attrs={'class': 'datetime-input'})
        }

class DiagnosticForm(forms.ModelForm):
    class Meta:
        model = Diagnostic
        fields = ['name', 'test_datetime', 'test_level']
        widgets = {
            'test_datetime': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }