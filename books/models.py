import datetime

from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_abstract = models.TextField(default='暂无信息', blank=True)
    book_catalog = models.TextField(default='暂无目录', blank=True)
    book_cover = models.CharField(max_length=256, default='', )
    book_author = models.CharField(max_length=200, default='')
    book_publisher = models.CharField(max_length=200, default='')
    book_isbn = models.CharField(max_length=256, default='')
    book_pub_date = models.DateField('data published', blank=True, default=datetime.date.today)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name

class BookQuote(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, default='', blank=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    reference = models.CharField(max_length=200, default='', blank=True)


# Create your models here.
