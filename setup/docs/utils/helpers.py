import json, datetime
from pathlib import Path
from django.conf import settings
from setup.docs.utils.naming_model import DeletedDocuments
from setup.docs.utils.naming import generate_id

BASE_DIR = Path(__file__).resolve().parent.parent

def move_to_deleted_document(table_name, id_no, object, deleted_by):
    data = {
        "id": generate_id(),
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


def get_static_path():
    if settings.DEBUG == True:
        return settings.STATICFILES_DIRS
    else:
        return settings.STATIC_ROOT

def get_coa_csv_path():
    return get_static_path()[0]+"/files/coa.csv"

def get_rcs_csv_path():
    return get_static_path()[0]+"/files/reason_codes.csv"