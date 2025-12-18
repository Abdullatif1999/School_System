from rest_framework.urls import path
from ..views.permission import ListPermissionGenericAPIView



urlpatterns = [
    path("" , ListPermissionGenericAPIView.as_view()),
    # path("login" , LoginUserGenericAPIView.as_view()),
    ]

