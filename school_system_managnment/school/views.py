from django.shortcuts import render
from rest_framework.generics import  GenericAPIView
from rest_framework.permissions import IsAuthenticated
from user.services import TokenService
from .serializer import CreateSchoolSerializer  , RetrieveSchoolSerializer
from rest_framework.response import Response
from .permisisons import Retreive_School
from .models import School
from rest_framework import status
from django.shortcuts import get_object_or_404
class CreateSchoolGenericAPIView(GenericAPIView):
    serializer_class = CreateSchoolSerializer
    def post(self , request):
        serializer = CreateSchoolSerializer(data =request.data , context = {'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = TokenService(user).getToken()
        return Response(data={"token":tokens},status=status.HTTP_201_CREATED)



class RetrieveSchoolAPIView(GenericAPIView):
    serializer_class = RetrieveSchoolSerializer
    permission_classes = [IsAuthenticated , Retreive_School]
    def get(self,request):
            instance = get_object_or_404(School.objects.filter(id=self.request.user.school.id))
            serializer = RetrieveSchoolSerializer(instance)
            return Response(serializer.data)
