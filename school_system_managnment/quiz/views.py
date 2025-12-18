from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Quiz
from .serializer.quizSerializer import CreateQuizSerializer  , RetreiveQuizSerializer , ListQuizSerializer , UpdateQuizSerializer
from django.shortcuts import get_list_or_404 , get_object_or_404
from .permissions import Add_Quiz , Change_Quiz , Destroy_Quiz , View_Quiz
from rest_framework.permissions import IsAuthenticated
class CreateQuizGenericAPIView(GenericAPIView):
    serializer_class = CreateQuizSerializer
    permission_classes = [IsAuthenticated , Add_Quiz]
    def post(self , request):
        serializer = CreateQuizSerializer(data = request.data , context = {'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    


class RetreiveQuizGenericAPIView(GenericAPIView):
    serializer_class = RetreiveQuizSerializer
    permission_classes = [IsAuthenticated , View_Quiz]
    def get(self , request , pk):
        quiz = get_object_or_404(Quiz.objects.filter(id = pk , school = request.user.school))
        serializer = RetreiveQuizSerializer(quiz)
        return Response(serializer.data)
    
    
class ListQuizGenericAPIView(GenericAPIView):
    serializer_class = ListQuizSerializer
    permission_classes = [IsAuthenticated , View_Quiz]
    def get(self , request):
        quizes = get_list_or_404(Quiz.objects.filter(school = request.user.school))
        serializer = ListQuizSerializer(quizes , many=True)
        return Response(serializer.data)
    

class UpdateQuizGenericAPIView(GenericAPIView):
        serializer_class = UpdateQuizSerializer
        permission_classes = [IsAuthenticated , Change_Quiz]
        def put(self , request , pk):
            quiz = get_object_or_404(Quiz.objects.filter(id = pk , school = request.user.school))
            serializer = UpdateQuizSerializer(quiz , data = request.data , context = {'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status= status.HTTP_200_OK)
        

class DeleteQuizGenericAPIView(GenericAPIView):
    serializer_class = RetreiveQuizSerializer
    permission_classes = [IsAuthenticated , Destroy_Quiz]
    def delete(self , request , pk):
        quiz = get_object_or_404(Quiz.objects.filter(id = pk , school = request.user.school))
        serializer_data = RetreiveQuizSerializer(quiz).data
        quiz.delete()
        return Response(serializer_data)
    