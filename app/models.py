from qux.core.models import CoreModel, default_null_blank
from django.db import models

app_name = 'library'


class Publisher(CoreModel):
    slug = models.SlugField(max_length=32, unique=True)
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=1024)
    email = models.EmailField(max_length=1024)

    class Meta:
        db_table = 'publisher'


class Author(CoreModel):
    slug = models.SlugField(max_length=32, unique=True)
    first_name = models.CharField(max_length=32, **default_null_blank)
    middle_name = models.CharField(max_length=32, **default_null_blank)
    last_name = models.CharField(max_length=32, **default_null_blank)
    url = models.URLField(max_length=1024, **default_null_blank)
    wikipedia = models.URLField(max_length=1024, **default_null_blank)

    class Meta:
        db_table = 'author'

    def __repr__(self):
        return f"<{self.slug}>"

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.slug} ({self.last_name}, {self.first_name})"
        elif self.first_name:
            return f"{self.slug} ({self.first_name})"
        else:
            return f"{self.slug}"


class Genre(CoreModel):
    slug = models.SlugField(max_length=32, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField(**default_null_blank)

    class Meta:
        db_table = 'genre'


class Book(CoreModel):
    slug = models.SlugField(max_length=32, unique=True)
    title = models.CharField(max_length=64)
    series = models.CharField(max_length=64, **default_null_blank)
    sequence = models.IntegerField(**default_null_blank)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, **default_null_blank)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, **default_null_blank)
    pubdate = models.DateField(**default_null_blank)
    isbn = models.CharField(max_length=13, **default_null_blank)
    asin = models.CharField(max_length=10, **default_null_blank)

    class Meta:
        db_table = 'book'
