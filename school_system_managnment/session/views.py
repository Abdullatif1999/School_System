from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Session
from .serializer import CreateSessionSerializer,UpdateSessionSerializer,ListSessionSerializer,RetreiveSessionSerializer
from django.shortcuts import get_list_or_404 , get_object_or_404
from .permissions import Add_Session,Change_Session,Destroy_Session,View_Session
from rest_framework.permissions import IsAuthenticated
class CreateSessionGenericAPIView(GenericAPIView):
    serializer_class = CreateSessionSerializer
    permission_classes = [Add_Session]
    def post(self , request):
        serializer = CreateSessionSerializer(data = request.data , context = {'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
class RetrieveSessionGenericAPIView(GenericAPIView):
    serializer_class = RetreiveSessionSerializer
    permission_classes = [IsAuthenticated , View_Session]
    def get(self , request , pk):
        session = get_object_or_404(Session.objects.filter(id=pk , school=self.request.user.school))
        serializer = RetreiveSessionSerializer(session)
        return Response(data = serializer.data)

class UpdateSessionGenericAPIView(GenericAPIView):
    queryset = Session.objects.all()
    serializer_class = UpdateSessionSerializer
    permission_classes = [IsAuthenticated , Change_Session]
    def put(self , request , pk):
        session = get_object_or_404(Session.objects.filter(id=pk , school=self.request.user.school))
        serializer = UpdateSessionSerializer(session , data= request.data , context = {'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)      


class DeleteSessionGenericAPIView(GenericAPIView):
    serializer_class = RetreiveSessionSerializer
    permission_classes = [IsAuthenticated , Destroy_Session]
    def delete(self , request , pk):
        session = get_object_or_404(Session.objects.filter(id=pk , school=self.request.user.school))
        serializer_data = RetreiveSessionSerializer(session).data
        session.delete()
        return Response(data = serializer_data)




class ListSessionGenericAPIView(GenericAPIView):
    serializer_class = ListSessionSerializer
    permission_classes = [IsAuthenticated , View_Session]
    def get(self , request):
        sessions = get_list_or_404(Session.objects.filter(school = request.user.school))
        serializer = ListSessionSerializer(sessions,many=True,context={'request':request})
        return Response(serializer.data)