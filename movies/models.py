import datetime

from django.db import models


class Movie(models.Model):
    # 基础数据
    movie_name = models.CharField(max_length=200)
    movie_abstract = models.TextField(default='暂无信息', blank=True)
    movie_type = models.CharField(max_length=50)
    movie_cover = models.CharField(max_length=256, default='', )
    movie_director = models.CharField(max_length=200, blank=True)
    movie_screenwriter = models.CharField(max_length=200, blank=True)
    movie_starring = models.CharField(max_length=200, blank=True)
    movie_cr = models.CharField(max_length=200, blank=True)  # 制片国家/地区
    movie_pub_date = models.DateField(
        'data published', blank=True, default=datetime.date.today)

    # 电影
    movie_minutes = models.IntegerField(blank=True, null=True)

    # 电视剧
    movie_episodes = models.IntegerField(blank=True, null=True)
    movie_episode_minutes = models.IntegerField(blank=True, null=True)

    # 元数据
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie_name


class MovieQuote(models.Model):
    content = models.TextField()
    reference = models.CharField(max_length=200, default='', blank=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
