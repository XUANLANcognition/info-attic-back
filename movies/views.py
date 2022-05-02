from movies.models import Movie, MovieQuote

from rest_framework import serializers
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters as filter_drf
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters

# Create your views here.

# Movie API


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'url', 'movie_name', 'movie_type', 'movie_cover', 'movie_director', 'movie_screenwriter',
                  'movie_starring', 'movie_cr', 'movie_pub_date', 'movie_minutes', 'movie_episodes', 'movie_episode_minutes', 'movie_abstract', 'pub_date')


class MovieFilter(filters.FilterSet):

    class Meta:
        model = Movie
        fields = '__all__'


class MoviePagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 128

    class Meta:
        model = Movie
        fields = '__all__'


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all().order_by('-pub_date')
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    filter_backends = (filters.DjangoFilterBackend, filter_drf.SearchFilter)
    search_fields = ('movie_name', )
    filterset_class = MovieFilter
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# MovieQuote API

class MovieQuoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MovieQuote
        fields = ('id', 'url', 'pub_date', 'reference', 'content')


class MovieQuoteFilter(filters.FilterSet):

    class Meta:
        model = MovieQuote
        fields = '__all__'


class MovieQuotePagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 128

    class Meta:
        model = MovieQuote
        fields = '__all__'


class MovieQuoteList(generics.ListCreateAPIView):
    queryset = MovieQuote.objects.all().order_by('-pub_date')
    serializer_class = MovieQuoteSerializer
    pagination_class = MovieQuotePagination
    filter_backends = (filters.DjangoFilterBackend, filter_drf.SearchFilter)
    search_fields = ('content', 'reference')
    filterset_class = MovieQuoteFilter
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieQuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieQuote.objects.all()
    serializer_class = MovieQuoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
