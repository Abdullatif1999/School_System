from rest_framework.urls import path
from .views import (CreateQuizGenericAPIView ,
                     RetreiveQuizGenericAPIView, 
                     ListQuizGenericAPIView , 
                    UpdateQuizGenericAPIView 
                    , DeleteQuizGenericAPIView
                    )



urlpatterns = [
    path("create" , CreateQuizGenericAPIView.as_view()),
    path("<int:pk>" , RetreiveQuizGenericAPIView.as_view()),
    path("update/<int:pk>" , UpdateQuizGenericAPIView.as_view()),
    path("" , ListQuizGenericAPIView.as_view()),
    path("delete/<int:pk>" , DeleteQuizGenericAPIView.as_view())
    ]


