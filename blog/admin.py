from django.contrib import admin

from .models import Tag, Author, Post, Comments


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "author", "date")
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user_name", "post"]


admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentAdmin)