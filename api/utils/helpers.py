import random
from pathlib import Path
import os
from django.conf import settings
from django.db.models import query

from api.models.domains_model import Domain
from api.models.system_model import DeletedDocuments

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


def get_user_domain(user, domain, company=None):
    condition1 = ""
    if not company: 
        condition1 = 'company = "{}"'.format(company)

    condition2 = ""
    if not user: 
        condition2 = 'user_id="{}"'.format(user)

    query = """
        select 
    
    """

    domain = Domain.objects.raw(query)


def move_to_deleted_document(table_name, id_no, object, deleted_by):
    data = {
        "table_name": table_name,
        "id_no": id_no,
        "object": object,
        "deleted_by": deleted_by
    }
    DeletedDocuments.objects.create(**data)
    return True