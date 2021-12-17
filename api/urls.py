from django.urls import path

from api.views.defaults_view import SetupDefaultsView 
# from . import views


#/api/method
urlpatterns = [
    path('setup', SetupDefaultsView.as_view(), name='setups_default'),
    path('setup/<company_code>', SetupDefaultsView.as_view(), name='get_setups_default'),
]
