from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    
    readonly_fields = ("slug",)
    list_display = ("title", "author", "date")
    list_filter = ("author", "date", "tags")

class CommentAdmin(admin.ModelAdmin):

    list_display = ("post", "username", "comment")
    list_filter = ("username", "post")

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(CommentModel, CommentAdmin)