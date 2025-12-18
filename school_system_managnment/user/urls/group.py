from rest_framework.urls import path
from ..views.group import ListGroupGenericAPIView , CreateGroupGenericAPIView , UpdateGroupGenericAPIView , DeleteGroupAPIView , RetreiveGroupGenericAPIView


urlpatterns = [
    path("" , ListGroupGenericAPIView.as_view()),
    path("create" , CreateGroupGenericAPIView.as_view()),
    path("update/<int:pk>" , UpdateGroupGenericAPIView.as_view()),
    path("<int:pk>" , RetreiveGroupGenericAPIView.as_view()),
    path("delete/<int:pk>" , DeleteGroupAPIView.as_view()),
    ]

