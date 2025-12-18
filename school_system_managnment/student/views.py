from django.shortcuts import render
from .serializer import CreateStudentSerializer , ListStudentSerializer , RetreiveStudentSerializer , UpdateStudentSerializer , CreateUserStudentSerializer
from rest_framework.generics import GenericAPIView
from .models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import Add_Student , Change_Student , Destroy_Student , View_Student , Add_User_Student
from django.shortcuts import get_list_or_404 , get_object_or_404
class CreateStudentGenericAPIView(GenericAPIView):
    serializer_class = CreateStudentSerializer
    permission_classes = [IsAuthenticated , Add_Student]
    def post(self , request):
        serializer = CreateStudentSerializer(data = request.data , context = {'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
class CreateUserStudentGenericAPIView(GenericAPIView):
    serializer_class = CreateUserStudentSerializer
    permission_classes = [IsAuthenticated , Add_User_Student]
    def put(self , request , pk):
        student = get_object_or_404(Student.objects.filter(id = pk , school = request.user.school))
        serializer = CreateUserStudentSerializer(student , data = request.data , context = {'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

        
class ListStudentGenericAPIView(GenericAPIView):
    serializer_class = ListStudentSerializer
    permission_classes = [IsAuthenticated , View_Student]

    def get(self , request):
        students = get_list_or_404(Student.objects.filter(school = request.user.school))
        serializer = ListStudentSerializer(students , many=True)
        return Response(serializer.data)
    
class RetieveStudentGenericAPIView(GenericAPIView):
    serializer_class = RetreiveStudentSerializer
    permission_classes = [IsAuthenticated , View_Student]
    def get(self , request , pk):
        student  = get_object_or_404(Student.objects.filter(id=pk , school = request.user.school))
        serializer = RetreiveStudentSerializer(student)
        return Response(serializer.data)
    
class UpdateStudentGenericAPIView(GenericAPIView):
    serializer_class = UpdateStudentSerializer
    permission_classes = [IsAuthenticated , Change_Student]
    def put(self , request , pk):
        student  = get_object_or_404(Student.objects.filter(id=pk , school = request.user.school))
        serializer = UpdateStudentSerializer(student , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
class DeleteStudentGenericAPIView(GenericAPIView):
    serializer_class = RetreiveStudentSerializer
    permission_classes = [IsAuthenticated , Destroy_Student]
    def delete(self , request , pk):
        student  = get_object_or_404(Student.objects.filter(id=pk , school = request.user.school))
        serializer = RetreiveStudentSerializer(student)
        student.delete()
        return Response(serializer.data , status=status.HTTP_200_OK)