from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from django.contrib.auth.models import Group
from ..serializer.group import ListGroupSerializer , CreateGroupSerializer , UpdateGroupSerializer , RetreiveGroupSerializer


class ListGroupGenericAPIView(GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = ListGroupSerializer
    def get(self , request):
        groups = Group.objects.all()
        serializer = ListGroupSerializer(groups , many = True)
        return Response(serializer.data)
    
class RetreiveGroupGenericAPIView(GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = RetreiveGroupSerializer
    def get(self , request , pk):
        group = self.get_object()
        serializer = RetreiveGroupSerializer(group)
        return Response(serializer.data)


class CreateGroupGenericAPIView(GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = CreateGroupSerializer
    def post(self , request):
        serializer = CreateGroupSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    

class UpdateGroupGenericAPIView(GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = UpdateGroupSerializer
    def put(self , request , pk):
        group = self.get_object()
        serializer = UpdateGroupSerializer(group , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
class DeleteGroupAPIView(APIView):

    def delete(self , request , pk):
        group = Group.objects.get(id = pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)