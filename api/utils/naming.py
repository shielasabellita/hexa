from django.http import response
from api.models import Series
from rest_framework.response import Response


def get_prefix(id, no_of_zeroes=9):
    try:
        series = Series.objects.get(id=id)
        return series
    except:
        data = {
            "id": id,
            "no_of_zeroes": no_of_zeroes,
            "current": 0
        }
        series = Series.objects.create(**data)
        return series


def set_naming_series(id, is_series=True, no_of_zeroes=9):
    if is_series:
        try:
            series = get_prefix(id, no_of_zeroes=no_of_zeroes)
                
            ctr = series.current + 1
            
            series.current = ctr
            series.save()

            zero_fill = str(ctr).zfill(series.no_of_zeroes)
            
            name = "{}_{}".format(series.id, zero_fill)
            return name

        except Exception as e:
            return False
            