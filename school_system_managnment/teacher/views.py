from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from .models import Teacher
from .serializer import CreateTeacherSerializer , UpdateTeacherSerializer , RetreiveTeacherSerializer , ListTeacherSerializer , CreateUserTeacherSerializer
from .permissions import Add_Teacher , Change_Teacher ,Destroy_Teacher , View_Teacher , Add_User_Teacher
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import  get_list_or_404 , get_object_or_404

class CreateTeacherGenericAPIView(GenericAPIView):
    serializer_class = CreateTeacherSerializer
    pagination_class = [IsAuthenticated , Add_Teacher]
    def post(self , request):
        serializer = CreateTeacherSerializer(data = request.data , context = {'request' : request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    

class ListTeacherGenericAPIView(GenericAPIView):
    serializer_class = ListTeacherSerializer
    pagination_class = [IsAuthenticated , View_Teacher]
    def get(self , request):
        teachers = get_list_or_404(Teacher.objects.filter(school = request.user.school))
        serializer = ListTeacherSerializer(teachers , many=True)
        return Response(serializer.data)
    
class RetreiveTeacherGenericAPIView(GenericAPIView):
    serializer_class = RetreiveTeacherSerializer
    pagination_class = [IsAuthenticated , View_Teacher]
    def get(self , request, pk):
        teacher = get_object_or_404(Teacher.objects.filter(id=pk,school=request.user.school))
        serializer = RetreiveTeacherSerializer(teacher)
        return Response(serializer.data)
    

class UpdateTeacherGenericAPIView(GenericAPIView):
    serializer_class = UpdateTeacherSerializer
    pagination_class = [IsAuthenticated , Change_Teacher]
    def put(self , request , pk):
        teacher = get_object_or_404(Teacher.objects.filter(id=pk,school=request.user.school))
        serializer = UpdateTeacherSerializer(teacher , data = request.data , context = {'request' : request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
class DeleteTeacherGenericAPIView(GenericAPIView):
    serializer_class = RetreiveTeacherSerializer
    pagination_class = [IsAuthenticated , Destroy_Teacher]
    def delete(self , request , pk):
        teacher = get_object_or_404(Teacher.objects.filter(id=pk,school=request.user.school))
        serializer_data = RetreiveTeacherSerializer(teacher).data
        teacher.delete()
        return Response(serializer_data,status=status.HTTP_200_OK)
    
class CreateUserTeacherGenericAPIView(GenericAPIView):
    serializer_class = CreateUserTeacherSerializer
    permission_classes = [IsAuthenticated , Add_User_Teacher]
    def put(self , request , pk):
        instance = get_object_or_404(Teacher.objects.filter(id=pk , school = request.user.school))
        serializer = CreateUserTeacherSerializer(instance , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)