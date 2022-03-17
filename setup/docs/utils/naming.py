import traceback
from setup.docs.utils.naming_model import Series

import uuid


def generate_id():
    """
        For PK id
        a 32-characted hexadecimal string
    """
    return uuid.uuid4().hex


def set_naming_series(id, is_series=True):
    """
        set code or naming series
        format: CODE_{9}
        no of zeroes: 9 because of {9}
    """
    if is_series:
        validated_code = get_prefix_and_zeroes(id)
        series = get_prefix_inst(validated_code[0], validated_code[1])
            
        ctr = series.current + 1
        
        series.current = ctr
        series.save()

        zero_fill = str(ctr).zfill(series.no_of_zeroes)
        
        name = "{}{}".format(series.id, zero_fill)
        return str(name)


def get_prefix_inst(id, no_of_zeroes=9):
    try:
        series = Series.objects.get(id=id)
        return series
    except:
        try:
            data = {
                "id": id,
                "no_of_zeroes": no_of_zeroes,
                "current": 0
            }
            series = Series.objects.create(**data)
            return series
        except Exception as e:
            traceback.print_exc()

def get_prefix_and_zeroes(code):
    if code.count("{") > 1 or code.count("}") > 1:
        raise Exception("Code must not include special characters")
    else:
        start = code.find("{")
        end = code.find("}")

        return code[:start], int(code[start+1:end])