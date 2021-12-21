from django.urls import path

from api.views.defaults_view import SetupDefaultsView
from api.views.views import TestView, TestViewCSV
# from . import views


#/api/method
urlpatterns = [
    # test 
    path('test', TestView.as_view(), name='test_view'),
    path('test_csv', TestViewCSV.as_view(), name='test_view_csv'),
    
    path('setup', SetupDefaultsView.as_view(), name='setups_default'),
    path('setup/<company_code>', SetupDefaultsView.as_view(), name='get_setups_default'),
    
]
