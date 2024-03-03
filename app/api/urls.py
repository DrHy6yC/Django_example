from django.urls import path, include

from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'quize', views.QuizeViewSet)
router.register(r'constant', views.ConstantViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'), name='api_auth'),
]
