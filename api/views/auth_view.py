from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_202_ACCEPTED, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView
# from rest_framework.decorators import api_view

# serializers
from api.serializers import StatusAndReasonCodeSerializer

# models
from api.models import StatusAndRCode


class StatusAndReasonCodeView(APIView):

    def get(self, request, format=None):
        status_and_reason_codes = StatusAndRCode.objects.all()
        serializer = StatusAndReasonCodeSerializer(status_and_reason_codes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StatusAndReasonCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)