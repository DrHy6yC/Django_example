
from django.urls import path, include

from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'constant', views.ConstantViewSet)
router.register(r'acces_user', views.AccesUserViewSet)
router.register(r'level_user', views.LevelUserViewSet)
router.register(r'status_quize', views.StatusQuizeViewSet)
router.register(r'quize', views.QuizeViewSet)
router.register(r'quize_answer', views.QuizeAnswerViewSet)
router.register(r'quize_question', views.QuizeQuestionViewSet)
router.register(r'quize_true_answer', views.QuizeTrueAnswerViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'user_quize', views.UserQuizeViewSet)
router.register(r'user_answer', views.UserAnswerViewSet)

app_name = 'api'

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'), name='api_auth'),
]
