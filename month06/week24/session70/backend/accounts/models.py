from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Нэмэлт талбаруудтай Custom User model"""
    
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Email-ээр нэвтрэх
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = 'Хэрэглэгч'
        verbose_name_plural = 'Хэрэглэгчид'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.email