from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from django.contrib.auth.models import Permission
from ..serializer.permission import ListPermissionSerializer
from ..permissions.permission import View_Permission
from rest_framework.permissions import IsAuthenticated
class ListPermissionGenericAPIView(GenericAPIView):
    queryset = Permission.objects.all()
    serializer_class = ListPermissionSerializer
    permission_classes = [IsAuthenticated , View_Permission]
    def get(self , request):
        permissions = Permission.objects.all()
        serializer = ListPermissionSerializer(permissions , many = True)
        return Response(serializer.data)
    


