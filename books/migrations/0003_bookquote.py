# Generated by Django 4.0.3 on 2022-03-25 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_book_author_book_book_cover_book_book_isbn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(default='', max_length=200)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]
