from rest_framework.urls import path
from .views import (CreateSessionGenericAPIView , RetrieveSessionGenericAPIView , ListSessionGenericAPIView , 
                    UpdateSessionGenericAPIView , DeleteSessionGenericAPIView)



urlpatterns = [
    path("create" , CreateSessionGenericAPIView.as_view()),
    path("<int:pk>" , RetrieveSessionGenericAPIView.as_view()),
    path("update/<int:pk>" , UpdateSessionGenericAPIView.as_view()),
    path("" , ListSessionGenericAPIView.as_view()),
    path("delete/<int:pk>" , DeleteSessionGenericAPIView.as_view())
    ]


