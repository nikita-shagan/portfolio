from django.contrib import admin

from .models import Profile, Work


@admin.register(Profile)
class CategoryAdmin(admin.ModelAdmin):
    """Admin settings for Profile model."""

    list_display = (
        'user',
        'job',
        'location',
        'avatar',
        'techs',
        'birth_date',
    )

    list_editable = (
        'job',
        'location',
    )

    list_display_links = ('user',)


@admin.register(Work)
class PostAdmin(admin.ModelAdmin):
    """Admin settings for Work model."""

    list_display = (
        'title',
        'description',
        'image',
        'created_at',
    )
