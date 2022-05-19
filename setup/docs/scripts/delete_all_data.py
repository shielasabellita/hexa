from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db import connection


@api_view(['POST'])
def wipe_all_data(request):
    """
        expected payload
        {
            "confirm": 1 or 0,
            "usr": 
        }
    """
    
    data = request.data
    delete_data()
    return Response("Successfully truncated all data")
    


def delete_data():
    tables = connection.introspection.table_names()

    excluded_tables = ['auth_group', 'auth_group_permissions', 'auth_permission', 'auth_user', 
    'auth_user_groups', 'auth_user_user_permissions', 'authtoken_token', 
    'django_admin_log', 'django_content_type', 'django_migrations', 'django_session']

    for t in tables: 
        if t not in excluded_tables:
            cursor = connection.cursor()
            cursor.execute("SET GLOBAL FOREIGN_KEY_CHECKS=0")
            cursor.execute("TRUNCATE TABLE `{}`".format(t))
            cursor.execute("SET GLOBAL FOREIGN_KEY_CHECKS=1")

