from django.shortcuts import render
from .models import Clas
from rest_framework.generics import GenericAPIView
from .serializer import CreateClasSerializer ,ListClasSerializer , UpdateClasSerializer , RetreiveClasSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import Add_clas , Change_clas , Destroy_clas , View_clas
from django.shortcuts import get_list_or_404 , get_object_or_404

class CreateClasGenericAPIView(GenericAPIView):
    serializer_class = CreateClasSerializer
    permission_classes = [IsAuthenticated , Add_clas]
    def post(self , request):
        serializer = CreateClasSerializer(data = request.data , context = request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    


class ListClasGenericAPIView(GenericAPIView):
    serializer_class = ListClasSerializer(many = True)
    permission_classes = [IsAuthenticated , View_clas]
    def get(self , request):
        classes = get_list_or_404(Clas.objects.filter(school = request.user.school))
        serializer = ListClasSerializer(classes , many = True)
        return Response(serializer.data)
    


class UpdateClasGenericAPIView(GenericAPIView):
    serializer_class = UpdateClasSerializer
    permission_classes = [IsAuthenticated , Change_clas]
    def post(self , request , pk):
        clas = get_object_or_404(Clas.objects.filter(id = pk , school = request.user.school))
        serializer = UpdateClasSerializer(clas , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    


class RetreiveClasGenericAPIView(GenericAPIView):
    serializer_class = RetreiveClasSerializer
    permission_classes = [IsAuthenticated , View_clas]  
    def get(self , request , pk):
        clas = get_object_or_404(Clas.objects.filter(id = pk , school = request.user.school))
        serializer = RetreiveClasSerializer(clas)
        return Response(serializer.data)



class DeleteClasGenericAPIView(GenericAPIView):
    serializer_class = RetreiveClasSerializer
    permission_classes = [IsAuthenticated , Destroy_clas]
    def delete(self , request , pk):
        clas = get_object_or_404(Clas.objects.filter(id = pk , school = request.user.school))
        serializer = RetreiveClasSerializer(clas)
        clas.delete()
        return Response(serializer.data , status=status.HTTP_200_OK)