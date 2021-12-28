import random
from pathlib import Path
import os
from django.conf import settings

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