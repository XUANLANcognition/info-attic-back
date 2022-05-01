from django.urls import include, path
from rest_framework import routers

from movies.views import MovieList, MovieDetail, MovieQuoteList, MovieQuoteDetail

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>', MovieDetail.as_view(), name='movie-detail'),
    path('moviequotes/', MovieQuoteList.as_view(), name='moviequote-list'),
    path('moviequotes/<int:pk>', MovieQuoteDetail.as_view(), name='moviequote-detail'),
]