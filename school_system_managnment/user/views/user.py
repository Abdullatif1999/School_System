from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from ..serializer.user import CreateUserSerializer  , RetreiveUserSerializer , LoginUserSerializer
from ..services import TokenService
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from django.contrib.auth import authenticate


class CreateUserGenericAPIView(GenericAPIView):
    serializer_class = CreateUserSerializer
    def post(self , request):
        data = request.data
        serializer = CreateUserSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = TokenService(user).getToken()
        response = {"user":RetreiveUserSerializer(user).data ,
                    "tokens": tokens}
        return Response(response , status=status.HTTP_201_CREATED)


        
class LoginUserGenericAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginUserSerializer
    
    def post(self , request):
        user = authenticate(email = request.data['email'] , password = request.data['password'])
        if user:
            tokens = TokenService(user).getToken()
            response = {"user":RetreiveUserSerializer(user).data ,
                    "tokens": tokens}
            return Response(response)
        return Response(status=status.HTTP_404_NOT_FOUND , data={"email or password is incorrect please try again"})
    


class RetreiveUserGenericAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RetreiveUserSerializer

    def get(self , request , pk):
        user = self.get_object()
        serializer = RetreiveUserSerializer(user)
        return Response(serializer.data)