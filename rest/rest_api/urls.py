from rest_api.views import HumanQueryViewSet, AIResponseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'human_query', HumanQueryViewSet, basename='human_query')
router.register(r'ai_response', AIResponseViewSet, basename='ai_response')
urlpatterns = router.urls