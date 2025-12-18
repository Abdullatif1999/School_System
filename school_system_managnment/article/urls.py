from rest_framework.urls import path
from .views import CreateArticleGenericAPIView , RetreiveArticleGenericAPIView , ListArticleGenericAPIView , UpdateArticleGenericAPIView , DeleteArticleGenericAPIView

urlpatterns = [
    path("create" , CreateArticleGenericAPIView.as_view()),
    path("" , ListArticleGenericAPIView.as_view()),
    path("update/<int:pk>" ,UpdateArticleGenericAPIView.as_view()),
    path("<int:pk>" , RetreiveArticleGenericAPIView.as_view()),
    path("delete/<int:pk>" , DeleteArticleGenericAPIView.as_view())
    ]


