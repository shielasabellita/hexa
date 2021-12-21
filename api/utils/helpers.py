import random
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

def randomizer():
    ''''
        returns 7 random character
    '''
    rndm = ''.join(random.sample('0123456789qwertyuiopasdfghjklzxcvbnm', 7))
    return rndm


def get_static_path():
    return os.path.join(BASE_DIR, 'static')

def get_coa_csv_path():
    return get_static_path()+"/files/coa.csv"