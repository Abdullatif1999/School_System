from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializer import CreateVideoSerializer , UpdateVideoSerializer , RetreiveVideoSerializer , ListVideoSerializer
from .models import Video
import os
from rest_framework.permissions import IsAuthenticated
from .permissions import View_Video ,Add_Video,Change_Video,Destroy_Video
from django.shortcuts import get_list_or_404 , get_object_or_404


class CreateVideoGenericAPIView(GenericAPIView):
    serializer_class = CreateVideoSerializer
    permission_classes = [IsAuthenticated , Add_Video]
    def post(self , request):
        serializer = CreateVideoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    

class UpdateVideoGenericAPIView(GenericAPIView):
    serializer_class = UpdateVideoSerializer
    permission_classes = [IsAuthenticated , Change_Video]
    def put(self , request , pk):
        video = get_object_or_404(Video.objects.filter(id=pk , school = request.user.school))
        serializer = UpdateVideoSerializer(video,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    


class RetrieveVideoGenericAPIView(GenericAPIView):
    serializer_class = RetreiveVideoSerializer
    permission_classes = [IsAuthenticated , View_Video]
    def get(self , request , pk):
        video = get_object_or_404(Video.objects.filter(id=pk , school = request.user.school))
        serializer = RetreiveVideoSerializer(video , context = {'request':request})
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    

class ListVideoGenericAPIView(GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = ListVideoSerializer
    permission_classes = [IsAuthenticated,View_Video]  
    def get(self , request):
        videos = get_list_or_404(Video.objects.filter(school=request.user.school))
        serializer = ListVideoSerializer(videos,many=True,context = {'request':request})
        return Response(serializer.data , status=status.HTTP_200_OK)
    



class DeleteVideoGenericAPIView(GenericAPIView):
    serializer_class = RetreiveVideoSerializer
    permission_classes = [IsAuthenticated , Destroy_Video]
    def get(self , request , pk):
        video = get_object_or_404(Video.objects.filter(id=pk , school = request.user.school))
        serializer_data = RetreiveVideoSerializer(video , context = {'request':request}).data
        os.remove(video.media.file.path)
        video.media.delete()
        return Response(serializer_data , status=status.HTTP_200_OK)