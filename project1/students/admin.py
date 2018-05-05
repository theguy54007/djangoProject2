from django.contrib import admin

# Register your models here.
from .models import Student, Diagnostic

admin.site.register(Student)
admin.site.register(Diagnostic)