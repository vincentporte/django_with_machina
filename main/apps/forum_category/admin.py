from django.contrib import admin

from .models import ForumCategory


class ForumCategoryAdmin(admin.ModelAdmin):

    list_display = ("name",)
    list_display_links = ("name",)


admin.site.register(ForumCategory, ForumCategoryAdmin)
