from django.shortcuts import render
from .serializer import CreateSubjectSerializer , RetreiveSubjectSerializer , UpdateSubjectSerializer , ListSubjectSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Subject
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import Add_Subject , Change_Subject , Destroy_Subject , View_Subject
from django.shortcuts import get_list_or_404 , get_object_or_404
class CreateSubjectGenericAPIView(GenericAPIView):
    serializer_class = CreateSubjectSerializer
    permission_classes = [IsAuthenticated , Add_Subject]
    def post(self , request):
        serializer = CreateSubjectSerializer(data = request.data , context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    


class UpdateSubjectGenericAPIView(GenericAPIView):
    serializer_class = UpdateSubjectSerializer
    permission_classes = [IsAuthenticated , Change_Subject]
    def put(self , request , pk):
        subject = get_object_or_404(Subject.objects.filter(id=pk , clas__school = request.user.school))
        serializer = UpdateSubjectSerializer(subject,data = request.data , context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)



class RetreiveSubjectGenericAPIView(GenericAPIView):
    serializer_class = RetreiveSubjectSerializer
    permission_classes = [IsAuthenticated , View_Subject]
    def get(self , request , pk):
        subject = get_object_or_404(Subject.objects.filter(id=pk , clas__school = request.user.school))
        serializer = RetreiveSubjectSerializer(subject)
        return Response(serializer.data)
    


class ListSubjectGenericAPIView(GenericAPIView):
    serializer_class = ListSubjectSerializer
    permission_classes = [IsAuthenticated , View_Subject]
    def get(self , request):
        subjects = get_list_or_404(Subject.objects.filter(clas__school = request.user.school))
        serializer = ListSubjectSerializer(subjects , many=True)
        return Response(serializer.data)



class DeleteSubjectGenericAPIView(GenericAPIView):
    queryset = Subject.objects.all()
    serializer_class = RetreiveSubjectSerializer
    permission_classes = [IsAuthenticated , Destroy_Subject]
    def delete(self , request , pk):
        subject = get_object_or_404(Subject.objects.filter(id=pk , clas__school = request.user.school))
        serializer = RetreiveSubjectSerializer(subject)
        subject.delete()
        return Response(serializer.data , status=status.HTTP_200_OK)
