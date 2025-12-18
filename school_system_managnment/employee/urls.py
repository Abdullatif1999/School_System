from rest_framework.urls import path
from .views import (CreateEmployeeGenericAPIView , RetrieveEmployeeGenericAPIView , ListEmployeeGenericAPIView , 
                    UpdateEmployeeGenericAPIView , DeleteEmployeeGenericAPIView , CreateUserEmployeeGenericAPIView)



urlpatterns = [
    path("create" , CreateEmployeeGenericAPIView.as_view()),
    path("create/user/<int:pk>" , CreateUserEmployeeGenericAPIView.as_view()),
    path("<int:pk>" , RetrieveEmployeeGenericAPIView.as_view()),
    path("update/<int:pk>" , UpdateEmployeeGenericAPIView.as_view()),
    path("" , ListEmployeeGenericAPIView.as_view()),
    path("delete/<int:pk>" , DeleteEmployeeGenericAPIView.as_view())
    ]


