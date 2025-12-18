from rest_framework.urls import path
from .views import CreateClasGenericAPIView,ListClasGenericAPIView , UpdateClasGenericAPIView ,RetreiveClasGenericAPIView , DeleteClasGenericAPIView


urlpatterns = [
    path("create" , CreateClasGenericAPIView.as_view()),
    path("" , ListClasGenericAPIView.as_view()),
    path("update/<int:pk>" ,UpdateClasGenericAPIView.as_view()),
    path("<int:pk>" , RetreiveClasGenericAPIView.as_view()),
    path("delete/<int:pk>" , DeleteClasGenericAPIView.as_view())
    ]


