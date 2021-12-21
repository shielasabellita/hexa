from django.urls import path

from api.views.defaults_view import SetupDefaultsView
from api.views.views import TestView
# from . import views


#/api/method
urlpatterns = [
    # test 
    path('test', TestView.as_view(), name='test_view'),
    
    path('setup', SetupDefaultsView.as_view(), name='setups_default'),
    path('setup/<company_code>', SetupDefaultsView.as_view(), name='get_setups_default'),
    
]
