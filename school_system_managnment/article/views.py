from rest_framework.response import Response
from .models import Article
from rest_framework.generics import GenericAPIView 
from .serializer import CreateArticleSerializer , RetreiveArticleSerializer , ListArticleSerializer , UpdateArticleSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import Add_Article , Change_Article , Destroy_Article , View_Article
from django.shortcuts import get_list_or_404 , get_object_or_404
class CreateArticleGenericAPIView(GenericAPIView):
    serializer_class = CreateArticleSerializer
    permission_classes = [IsAuthenticated , View_Article]
    def post(self , request):
        serializer = CreateArticleSerializer(data = request.data , context={'request':request} )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class UpdateArticleGenericAPIView(GenericAPIView):
    serializer_class = UpdateArticleSerializer
    permission_classes = [IsAuthenticated , Change_Article]
    def put(self , request , pk):
        article = get_object_or_404(Article.objects.filter(id=pk , school = request.user.school))
        serializer = UpdateArticleSerializer(article , data = request.data , context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)



class RetreiveArticleGenericAPIView(GenericAPIView):
    serializer_class = RetreiveArticleSerializer
    permission_classes = [IsAuthenticated , View_Article]
    def get(self , request , pk):
        article = get_object_or_404(Article.objects.filter(id=pk , school = request.user.school))
        serializer = RetreiveArticleSerializer(article ,  context = {'request':request})
        return Response(serializer.data ,status=status.HTTP_200_OK)
    
class ListArticleGenericAPIView(GenericAPIView):
    serializer_class = ListArticleSerializer
    permission_classes = [IsAuthenticated , View_Article]
    def get(self , request):
        articles = get_list_or_404(Article.objects.filter(school = request.user.school))
        serializer = ListArticleSerializer(articles ,  context = {'request':request} , many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    
class DeleteArticleGenericAPIView(GenericAPIView):
    serializer_class = RetreiveArticleSerializer
    permission_classes = [IsAuthenticated , Destroy_Article]
    def delete(self , request , pk):
        article = get_object_or_404(Article.objects.filter(id=pk , school = request.user.school))
        serializer_data = RetreiveArticleSerializer(article ,  context = {'request':request}).data
        article.delete()
        return Response(serializer_data,status=status.HTTP_200_OK)
