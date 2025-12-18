from rest_framework.urls import path
from .views import CreateSubjectGenericAPIView , RetreiveSubjectGenericAPIView , UpdateSubjectGenericAPIView,DeleteSubjectGenericAPIView,ListSubjectGenericAPIView



urlpatterns = [
    path("create" , CreateSubjectGenericAPIView.as_view()),
    path("<int:pk>" , RetreiveSubjectGenericAPIView.as_view()),
    path("" , ListSubjectGenericAPIView.as_view()),
    path("update/<int:pk>" , UpdateSubjectGenericAPIView.as_view()),
    path("delete/<int:pk>",DeleteSubjectGenericAPIView.as_view())
    ]


