from rest_framework.urls import path
from .views import (CreateVideoGenericAPIView ,
                     RetrieveVideoGenericAPIView, 
                     ListVideoGenericAPIView , 
                    UpdateVideoGenericAPIView 
                    , DeleteVideoGenericAPIView
                    )



urlpatterns = [
    path("create" , CreateVideoGenericAPIView.as_view()),
    path("<int:pk>" , RetrieveVideoGenericAPIView.as_view()),
    path("update/<int:pk>" , UpdateVideoGenericAPIView.as_view()),
    path("" , ListVideoGenericAPIView.as_view()),
    path("delete/<int:pk>" , DeleteVideoGenericAPIView.as_view())
    ]


