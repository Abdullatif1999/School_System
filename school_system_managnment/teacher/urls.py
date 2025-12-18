from rest_framework.urls import path
from .views import (CreateTeacherGenericAPIView , RetreiveTeacherGenericAPIView , UpdateTeacherGenericAPIView
                    ,DeleteTeacherGenericAPIView,ListTeacherGenericAPIView , CreateUserTeacherGenericAPIView)



urlpatterns = [
    path("create" , CreateTeacherGenericAPIView.as_view()),
    path("<int:pk>" , RetreiveTeacherGenericAPIView.as_view()),
    path("user/<int:pk>" , CreateUserTeacherGenericAPIView.as_view()),
    path("" , ListTeacherGenericAPIView.as_view()),
    path("update/<int:pk>" , UpdateTeacherGenericAPIView.as_view()),
    path("delete/<int:pk>",DeleteTeacherGenericAPIView.as_view())
    ]


