from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    top_speed = models.IntegerField()


class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True, help_text="Enter unique genre")
    cat_description = models.CharField(max_length=100, help_text="A description of the genre", default='')

    def __str__(self):
        return self.cat_name


class Blogs(models.Model):
    bg_category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    bg_img = models.ImageField()
    bg_title = models.CharField(max_length=200)
    bg_content = models.TextField()
    bg_author = models.CharField(max_length=100)
    bg_upload_date = models.DateField()


class BlogManager(models.Manager):
    def get_genre_blogs(self, keyword):
        # return blogs from a specific genre
        return super().get_queryset().filter(bg_category=keyword)

    def get_author_blogs(self, keyword):
        # return blogs from a specific author
        return super().get_queryset().filter(bg_author=keyword)

# Create your models here.
