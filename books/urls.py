from django.urls import include, path
from rest_framework import routers

from books.views import BookList, BookDetail, BookQuoteList, BookQuoteDetail

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>', BookDetail.as_view(), name='book-detail'),
    path('bookquotes/', BookQuoteList.as_view(), name='bookquote-list'),
    path('bookquotes/<int:pk>', BookQuoteDetail.as_view(), name='bookquote-detail'),
]