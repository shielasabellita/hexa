from django.http import response
from api.models import Series
from rest_framework.response import Response



def set_naming_series(id, is_series=True):
    if is_series:
        try:
            series = Series.objects.get(id=id)
            ctr = series.current + 1
            
            series.current = ctr
            series.save()

            zero_fill = str(ctr).zfill(series.no_of_zeroes)
            
            name = "{}_{}".format(series.id, zero_fill)
            return name

        except Exception as e:
            return False