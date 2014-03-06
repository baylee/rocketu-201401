from django.contrib import admin
from blog.models import BlogPost, Comment, BlogCategory, BlogTag


class CommentInlineAdmin(admin.TabularInline):
    model = Comment
    extra = 1


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "posted", "title", "author")
    search_fields = ("title", "author__username")
    inlines = [CommentInlineAdmin]
    readonly_fields = ("author",)
    filter_horizontal = ("tags",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory)
admin.site.register(Comment)
admin.site.register(BlogTag)