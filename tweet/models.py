from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tweet(models.Model):
    """
    Tweet model representing a user's post with optional photo
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    text = models.TextField(max_length=280, help_text="Maximum 280 characters")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username}: {self.text[:50]}{"..." if len(self.text) > 50 else ""}'
    
    def get_absolute_url(self):
        return reverse('tweet_list')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"