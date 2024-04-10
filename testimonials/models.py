"""Testimonial Model"""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Testimonial(models.Model):
    """Model for Testimonial"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonials")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ Show the testimonials in ascending order by created_on """
        ordering = ['created_on']

    def __str__(self):
        return f"Testimonial by {self.user}"
