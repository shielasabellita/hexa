from multiprocessing import AuthenticationError
from xml.dom import InvalidAccessErr
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from setup.docs.company.company_model import Company
from setup.docs.company.company_serializer import CompanySerializer
from setup.docs.company.company_view import CompanyView
from setup.docs.user.user_serializer import UserSerializer
from hashlib import blake2b
from hmac import compare_digest
from setup.docs.user.auth import _set_token
from setup.core.doc import Document




@api_view(["POST"])
def login(request):
    data = request.data
    if request.method == "POST":
        user = authenticate(username=data['usr'], password=data['pwd'])
        if user:
            token = Token.objects.filter(user=user)
            if token:
                jwt_token = _set_token(user, token[0].key)
            else:
                token = Token.objects.create(user=user)
                token.save()
                jwt_token = _set_token(user, token.key)

            request_data = set_user_return(user)
            request_data.update({
                "token": jwt_token,
                "company_details": get_company()
            })

            return Response(request_data)
        else:
            return Response('Invalid credentials', status.HTTP_401_UNAUTHORIZED)

def get_company():
    try:
        company = Company.objects.all()
        return CompanySerializer(company, many=True).data

    except Exception as e:
        return None


@api_view(['POST'])
def register(request):
    data = request.data
    try:
        serializer = UserSerializer()
        user = serializer.create(data)
        user = set_user_return(user)
        return Response(user)
    except Exception as e:
        return Response(str(e))


def set_user_return(user):
    serializer = UserSerializer(user)

    request_data = serializer.data  
    request_data.pop("password")
    return request_data