from rest_framework import routers
#from .views import ListEventsView
from .api import EventsViewset, TagsViewSet

router = routers.DefaultRouter()
router.register('events', EventsViewset, basename="Events")
router.register('tags', TagsViewSet, basename="Events")
router.register('categories', CategoryViewSet, basename="Categories")
urlpatterns = router.urls