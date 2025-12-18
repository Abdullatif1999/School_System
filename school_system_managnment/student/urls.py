from rest_framework.urls import path
from .views import (CreateStudentGenericAPIView , ListStudentGenericAPIView , RetieveStudentGenericAPIView , 
                    UpdateStudentGenericAPIView,DeleteStudentGenericAPIView , CreateUserStudentGenericAPIView)


urlpatterns = [
    path("create" , CreateStudentGenericAPIView.as_view()),
    path("" , ListStudentGenericAPIView.as_view()),
    path("<int:pk>" , RetieveStudentGenericAPIView.as_view()),
    path("create/user/<int:pk>" , CreateUserStudentGenericAPIView.as_view()),
    path("update/<int:pk>" , UpdateStudentGenericAPIView.as_view()),
    path("delete/<int:pk>" , DeleteStudentGenericAPIView.as_view())
    ]


 