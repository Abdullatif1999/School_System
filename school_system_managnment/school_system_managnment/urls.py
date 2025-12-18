
from django.contrib import admin
from django.urls import path , include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/' , include('user.urls.user')),
    path('permission/' , include('user.urls.permission')),
    path('group/' , include('user.urls.group')),
    path('employee/' , include('employee.urls')),
    path('school/' , include('school.urls')),
    path('student/' , include('student.urls')),
    path('clas/' , include('clas.urls')),
    path('subject/' , include('subject.urls')),
    path('teacher/' , include('teacher.urls')),
    path('session/' , include('session.urls')),
    path('article/' , include('article.urls')),
    path('video/' , include('video.urls')),
    path('quiz/' , include('quiz.urls')),
]



from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
urlpatterns += [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]

urlpatterns += path('silk/', include('silk.urls', namespace='silk')),