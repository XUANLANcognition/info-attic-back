from django.urls import include, path
from rest_framework import routers

from users.views import OwnerSerializer

from users.views import OwnerDetail

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('owner/<int:pk>', OwnerDetail.as_view(), name='user-detail'),
]