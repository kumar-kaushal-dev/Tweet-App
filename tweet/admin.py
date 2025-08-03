from django.contrib import admin
from .models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    """
    Enhanced admin interface for Tweet model
    """
    list_display = ('user', 'text_preview', 'has_photo', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('text', 'user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    list_per_page = 20
    
    def text_preview(self, obj):
        """Show preview of tweet text"""
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Tweet Preview'
    
    def has_photo(self, obj):
        """Show if tweet has photo"""
        return bool(obj.photo)
    has_photo.boolean = True
    has_photo.short_description = 'Has Photo'