from django.urls import path, include
from .docs.parent_company.parent_company_view import ParentCompanyView
from .docs.company.company_view import CompanyView
from .docs.accounting_period.accounting_period_view import AccountingPeriodView
from .docs.branch.branch_view import BranchView
from .docs.location.location_view import LocationView
from .docs.scripts.setup import SetupDefaultsView


urlpatterns = [
    # MD
    path("docs/parent_company", ParentCompanyView.as_view(), name='parent_company'),
    path("docs/company", CompanyView.as_view(), name='company'),
    path("docs/acc_period", AccountingPeriodView.as_view(), name='acc_period'),
    path("docs/branch", BranchView.as_view(), name='branch'),
    path("docs/location", LocationView.as_view(), name='location'),


    # setup
    path("", SetupDefaultsView.as_view(), name='setup'),


]