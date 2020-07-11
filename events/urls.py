from rest_framework import routers
#from .views import ListEventsView
from .api import EventsViewset, TagsViewSet, CityViewSet, CountryViewSet

router = routers.DefaultRouter()
router.register('events', EventsViewset, basename="Events")
router.register('tags', TagsViewSet, basename="Events")
router.register('city', CityViewSet, basename="Cities")
router.register('country', CountryViewSet, basename="Countries")
urlpatterns = router.urls