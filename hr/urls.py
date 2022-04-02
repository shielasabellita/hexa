from django.urls import path, include
from hr.docs.employee.employee_view import EmployeeView


urlpatterns = [
    # MD
    path("docs/employee", EmployeeView.as_view(), name="employee")
]
