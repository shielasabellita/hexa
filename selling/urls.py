from django.urls import path, include
from selling.docs.customer.customer_view import CustomerView



urlpatterns = [
    # MD
    path("docs/customer", CustomerView.as_view(), name='customer')
]