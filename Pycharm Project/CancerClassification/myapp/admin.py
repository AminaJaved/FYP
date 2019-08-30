from django.contrib import admin

from .models import Snippet,Cancer,visualise,Blog


admin.site.register(Snippet)

admin.site.register(Cancer)

admin.site.register(visualise)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)


