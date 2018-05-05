from django.urls import path

from . import views
from .views import create_student, update_student, delete_student, create_diagnostic, delete_diagnostic,update_diagnostic

app_name = 'students'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/', views.detail, name='detail'),
    path('new', views.create_student, name='create_student'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('<int:student_id>/ ', views.diagnostics, name='diagnostics'),
    path('<int:student_id>/new', views.create_diagnostic, name='create_diagnostic'),
    path('<int:student_id>/delete/<int:diagnostic_id>/', views.delete_diagnostic, name='delete_diagnostic'),
    path('<int:student_id>/update/<int:diagnostic_id>/', views.update_diagnostic, name='update_diagnostic'),
]
