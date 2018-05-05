from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import  Student, Diagnostic
from .forms import StudentForm, DiagnosticForm

# Create your views here.

def index(request):
    students = Student.objects.all
    context = {'students': students}

    return render(request, 'students/index.html', context)

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})


def create_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('students:index')

    return render(request, 'students/student-form.html',{'form': form})

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('students:index')

    return render(request, 'students/student-form.html', {'form': form, 'student': student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('students:index')
    return render(request, 'students/stud-delete-confirm.html', {'student': student})

def diagnostics(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    diagnostics = student.diagnostic_set.get

    return render(request, 'diagnostics/diagnostics.html', {'student': student, 'diagnostics': diagnostics})

def create_diagnostic(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    form = DiagnosticForm(request.POST or None)

    if form.is_valid():
        diagnostic = form.save(commit=False)
        diagnostic.student = student
        diagnostic.save()
        return HttpResponseRedirect(reverse('students:diagnostics', args=(student.id,)))

    return render(request, 'diagnostics/diagnostic-form.html',{'student': student, 'form': form})


def update_diagnostic(request, student_id, diagnostic_id):
    student = get_object_or_404(Student, pk=student_id)
    diagnostic = get_object_or_404(Diagnostic, pk=diagnostic_id)
    form = DiagnosticForm(request.POST or None, instance=diagnostic)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('students:diagnostics', args=(student.id,)))

    return render(request, 'diagnostics/diagnostic-form.html', {'student': student, 'form': form, 'diagnostic': diagnostic})


def delete_diagnostic(request, student_id, diagnostic_id):
    student = get_object_or_404(Student, pk=student_id)
    diagnostic = get_object_or_404(Diagnostic, pk=diagnostic_id)
    if request.method == 'POST':
        diagnostic.delete()
        return HttpResponseRedirect(reverse('students:diagnostics', args=(student.id,)))
    return render(request, 'diagnostics/diag-delete-confirm.html', {'student': student, 'diagnostic': diagnostic})