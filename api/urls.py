from django.urls import path

from api.views.accounting import *
from api.views.views import *
from api.views.stock import *
from api.views.auth_view import *
from api.views.buying import *
# from . import views


#/api/method
urlpatterns = [
    # test 
    path('test', TestView.as_view(), name='test_view'),
    path('test_csv', TestViewCSV.as_view(), name='test_view_csv'),
    path('test_auth', TestAuthentication.as_view(), name='test_auth'),

    # system
    path('login', LoginView.as_view(), name='login'),
    
    #settings
    path('setup', SetupDefaultsView.as_view(), name='setups_default'),
    path('setup/<company_code>', SetupDefaultsView.as_view(), name='get_setups_default'),
    path('company/<company_code>', CompanyView.as_view(), name='company_view'),
    path('accounting_period_list/<company_code>', AccountingPeriodView.as_view(), name='accounting_period_view'),
    path('coa_list/<company_code>', ChartOfAccountsView.as_view(), name='coa_view'),
    path('accounts/<location>', LocationBranchView.as_view(), name='location_branch'),

    # accounting group
    path('accounting/group/<group>', AccountingGroup.as_view(), name='accounting_group_view'),
    
    # stock module urls
    path('stock/category_management/<category>', CategoryManagement.as_view(), name='category_management'),
    path('stock/item', ItemView.as_view(), name='item'),
    path('stock/item/item_detail/<item_detail>', ItemDetailsView.as_view(), name='item_details'),

    # buying module
    path('buying/supplier', SupplierView.as_view(), name='supplier'),

    # hr module
    # path('hr/employee'),
    
]
