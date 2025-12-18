from rest_framework.urls import path
from ..views.user import CreateUserGenericAPIView , LoginUserGenericAPIView , RetreiveUserGenericAPIView



urlpatterns = [
    path("create" , CreateUserGenericAPIView.as_view()),
    path("login" , LoginUserGenericAPIView.as_view()),
    path("<str:pk>" , RetreiveUserGenericAPIView.as_view())
    ]

