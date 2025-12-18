from rest_framework.urls import path
from .views import CreateSchoolGenericAPIView , RetrieveSchoolAPIView



urlpatterns = [
    path("create" , CreateSchoolGenericAPIView.as_view()),
    path("my_school" , RetrieveSchoolAPIView.as_view())
    ]


