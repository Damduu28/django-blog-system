from django.contrib import admin

# Register your models here.
from .models import Topic, Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    
admin.site.register(Comment)
admin.site.register(Topic)