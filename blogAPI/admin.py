from django.contrib import admin
from .models import Blog, Category

# Register your models here.
@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "img_url", "author", "publish", "status")
    list_filter = ("status", "created", "publish", "author", "category")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)  # use a lookup widget.Better than a drop down
    date_hierarchy = "publish"
    ordering = ("status", "publish")
