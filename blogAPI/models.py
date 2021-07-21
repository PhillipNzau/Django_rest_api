from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class Car(models.Model):
    name = models.CharField(max_length=100)
    top_speed = models.IntegerField()


class Profile(models.Model):
    """A profile for a blog member"""

    pass


class Category(models.Model):
    cat_name = models.CharField(
        max_length=100, unique=True, help_text="Enter unique genre"
    )
    cat_description = models.CharField(
        max_length=100, help_text="A description of the genre", default=""
    )

    def __str__(self):
        return self.cat_name


class PublishedManager(models.Manager):
    """Iteract with the Published posts directly"""

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")

    def get_genre_blogs(self, keyword):
        # return blogs from a specific genre
        return super().get_queryset().filter(bg_category=keyword)

    def get_author_blogs(self, keyword):
        # return blogs from a specific author
        return super().get_queryset().filter(bg_author=keyword)


class Blog(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img_url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add saves date automatically while creating
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    objects = models.Manager()  # the default manager
    published = PublishedManager()  # custom model manager

    class Meta:
        # sort latest posts first when query to database is done hence -ve
        ordering = ("-publish",)

    def __str__(self):
        """human readable representation of blog"""
        return self.title
