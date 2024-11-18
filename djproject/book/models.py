from django.db import models
import uuid
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255, blank=False)
    desciption = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'author'
        verbose_name = 'author'
        verbose_name_plural = 'author'


class BookCategory(models.Model):
    category = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book_category'
        verbose_name = "book_category"           # Tên hiển thị cho một mục
        verbose_name_plural = "book_category"


class Book(models.Model):
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=False)
    authors = models.ManyToManyField(Author, blank=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    sold_quantity = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'
        verbose_name = "book"           # Tên hiển thị cho một mục
        verbose_name_plural = "book"

    def __str__(self):
        return self.title
