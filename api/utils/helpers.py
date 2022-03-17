import random
from pathlib import Path
import os
from xml.dom import NotFoundErr
from django.conf import settings
from django.db.models import query

from api.models import *
from api.serializers import *

import datetime, json


BASE_DIR = Path(__file__).resolve().parent.parent

def randomizer():
    ''''
        returns 7 random character
    '''
    rndm = ''.join(random.sample('0123456789qwertyuiopasdfghjklzxcvbnm', 7))
    return rndm


def get_static_path():
    if settings.DEBUG == True:
        return settings.STATICFILES_DIRS
    else:
        return settings.STATIC_ROOT

def get_coa_csv_path():
    return get_static_path()[0]+"/files/coa.csv"

def get_rcs_csv_path():
    return get_static_path()[0]+"/files/reason_codes.csv"


# def get_user_domain(user, domain, company=None):
#     condition1 = ""
#     if not company: 
#         condition1 = 'company = "{}"'.format(company)

#     condition2 = ""
#     if not user: 
#         condition2 = 'user_id="{}"'.format(user)

#     query = """
#         select 
    
#     """

#     domain = Domain.objects.raw(query)


def move_to_deleted_document(table_name, id_no, object, deleted_by):
    data = {
        "table_name": table_name,
        "id_no": id_no,
        "object": json.dumps(object,  default=converter),
        "deleted_by": deleted_by
    }
    DeletedDocuments.objects.create(**data)
    return True

def converter(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()


def get_company(company_code):
    try:
        company_inst = Company.objects.get(company_code=company_code)
        company_data = CompanySerializer(company_inst).data
        return company_data
    except NotFoundErr as e:
        return e


def get_doc(table, id):
    try:
        inst = table.objects.get(id=id)
        return inst
    except NotFoundErr as e:
        return "{} {} Instance Not Found".format(table, id)