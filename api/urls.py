from django.urls import path

from api.views.defaults_view import SetupDefaultsView
from api.views.company_view import CompanyView
from api.views.accounting_period_view import AccountingPeriodView
from api.views.chartofaccounts_view import ChartOfAccountsView
from api.views.views import TestView, TestViewCSV
from api.views.stock_module_view import *
# from . import views


#/api/method
urlpatterns = [
    # test 
    path('test', TestView.as_view(), name='test_view'),
    path('test_csv', TestViewCSV.as_view(), name='test_view_csv'),
    
    #settings
    path('setup', SetupDefaultsView.as_view(), name='setups_default'),
    path('setup/<company_code>', SetupDefaultsView.as_view(), name='get_setups_default'),
    path('company/<company_code>', CompanyView.as_view(), name='company_view'),
    path('accounting_period_list/<company_code>', AccountingPeriodView.as_view(), name='accounting_period_view'),
    path('coa_list/<company_code>', ChartOfAccountsView.as_view(), name='coa_view'),
    
    # stock module urls
    path('stock/item_category', ItemCategoryView.as_view(), name='item_category_view'),
    path('stock/item_category/brand', ItemCatBrandView.as_view(), name='item_brand_view'),
    path('stock/item_category/department', ItemCatDepartmentView.as_view(), name='item_dept_view'),
    path('stock/item_category/form', ItemCatFormView.as_view(), name='item_form_view'),
    path('stock/item_category/manufacturer', ItemCatManufacturerView.as_view(), name='item_manufacturer_view'),
    path('stock/item_category/section', ItemCatSectionView.as_view(), name='item_section_view'),
    path('stock/item_category/size', ItemCatSizeView.as_view(), name='item_size_view'),
]
