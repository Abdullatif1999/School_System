from django.shortcuts import render
from rest_framework.generics import GenericAPIView 
from .serializer import CreateEmployeeSerializer , RetrieveEmployeeSerializer , ListEmployeeSerializer,UpdateEmployeeSerializer,CreateUserEmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from .permissions import Add_Employee,Destroy_Employee,Change_Employee,View_Employee , Add_User_Employee
from .models import Employee
from django.shortcuts import get_object_or_404 , get_list_or_404
class CreateEmployeeGenericAPIView(GenericAPIView):
    serializer_class = CreateEmployeeSerializer
    permission_classes = [IsAuthenticated , Add_Employee]
    def post(self , request):
        serializer = CreateEmployeeSerializer(data = request.data , context = {'user':request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    


class RetrieveEmployeeGenericAPIView(GenericAPIView):
    serializer_class = RetrieveEmployeeSerializer
    permission_classes = [IsAuthenticated , View_Employee ]
    def get(self , request , pk):
        instance = get_object_or_404(Employee.objects.filter(id=pk , school = request.user.school))
        serializer = RetrieveEmployeeSerializer(instance)
        return Response(serializer.data)
    


class ListEmployeeGenericAPIView(GenericAPIView):
    serializer_class = ListEmployeeSerializer
    permission_classes = [IsAuthenticated ,View_Employee]
    def get(self , request):
        employees = get_list_or_404(Employee.objects.filter(school = request.user.school))
        serializer = ListEmployeeSerializer(employees,many=True)
        return Response(serializer.data)
    


class UpdateEmployeeGenericAPIView(GenericAPIView):
    serializer_class = UpdateEmployeeSerializer
    permission_classes = [IsAuthenticated ,Change_Employee]
    def put(self , request , pk):
        instance = get_object_or_404(Employee.objects.filter(id=pk , school = request.user.school))
        serializer = UpdateEmployeeSerializer(instance , data = request.data )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


class  DeleteEmployeeGenericAPIView(GenericAPIView):
    serializer_class = RetrieveEmployeeSerializer
    permission_classes = [IsAuthenticated ,Destroy_Employee]
    def delete(self , request , pk):
        instance = get_object_or_404(Employee.objects.filter(id=pk , school = request.user.school))
        serializer_data = RetrieveEmployeeSerializer(instance).data
        instance.delete()
        return Response(serializer_data , status=status.HTTP_200_OK)
    


class CreateUserEmployeeGenericAPIView(GenericAPIView):
    serializer_class = CreateUserEmployeeSerializer
    permission_classes = [IsAuthenticated , Add_User_Employee]
    def put(self , request , pk):
        instance = get_object_or_404(Employee.objects.filter(id=pk , school = request.user.school))
        serializer = CreateUserEmployeeSerializer(instance , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)