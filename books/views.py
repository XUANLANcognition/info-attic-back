from books.models import Book, BookQuote

from rest_framework import serializers
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters as filter_drf
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters

# Create your views here.

# Book API


class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'url', 'book_name', 'book_abstract', 'book_catalog', 'pub_date', 'book_cover',
                  'book_author', 'book_pub_date', 'book_isbn', 'book_publisher')


class BookFilter(filters.FilterSet):

    class Meta:
        model = Book
        fields = '__all__'


class BookPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 128

    class Meta:
        model = Book
        fields = '__all__'


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-pub_date')
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = (filters.DjangoFilterBackend, filter_drf.SearchFilter)
    search_fields = ('book_name', )
    filterset_class = BookFilter
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# BookQuote API

class BookQuoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BookQuote
        fields = ('id', 'url', 'content', 'pub_date', 'location', 'reference')


class BookQuoteFilter(filters.FilterSet):

    class Meta:
        model = BookQuote
        fields = '__all__'


class BookQuotePagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 128

    class Meta:
        model = BookQuote
        fields = '__all__'


class BookQuoteList(generics.ListCreateAPIView):
    queryset = BookQuote.objects.all().order_by('-pub_date')
    serializer_class = BookQuoteSerializer
    pagination_class = BookQuotePagination
    filter_backends = (filters.DjangoFilterBackend, filter_drf.SearchFilter)
    search_fields = ('content', 'reference')
    filterset_class = BookQuoteFilter
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookQuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookQuote.objects.all()
    serializer_class = BookQuoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
