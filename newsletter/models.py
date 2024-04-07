from django.db import models

# Create your models here.


class Subscribers(models.Model):
    """Model to store subscriber information"""
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    """Model to store mail message information"""
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title