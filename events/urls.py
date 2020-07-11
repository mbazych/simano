from rest_framework import routers
#from .views import ListEventsView
from .api import EventsViewset, TagsViewSet, CityViewSet, CountryViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('events', EventsViewset, basename="Events")
router.register('tags', TagsViewSet, basename="Events")
router.register('city', CityViewSet, basename="Cities")
router.register('country', CountryViewSet, basename="Countries")
router.register('category', CategoryViewSet, basename="Categories")
urlpatterns = router.urls