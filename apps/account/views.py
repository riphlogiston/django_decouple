from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .serializers import CustomAuthTokenSerializer, RegisterSerializer
from .services.utils import send_activate_code
from .models import CustomUser


class LoginView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer


class RegisterView(APIView):

    def post(self, request):
        data = request.POST  # (email=adadsd@mail.ru, password =!@#!@$@)
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.validated_data #dict <---- is_valid()
        user:CustomUser=serializer.save()
        send_activate_code(user.activate_code, user.email)
        return Response(serializer.data)

class ActivateView(APIView):
    #http://localhost:8000/api/v1/account/activate/sfshdkfhdskgsdh
    def get(self, request, activate_code):
        user=get_object_or_404(CustomUser, activate_code=activate_code)
        user.is_active=True
        user.save()
        return Response({"message":"all okey, your activate account"})

