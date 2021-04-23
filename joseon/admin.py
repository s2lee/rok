from django.contrib import admin
from .models import Post, Category, Comment

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'all_recommend', 'date_posted', 'political_orientation','total_credibility')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'contents', 'reply', 'reply_id', 'total', 'anonymous')
