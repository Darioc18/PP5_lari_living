"""imports for admin page"""

from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """Allows admin to manage Testimonials in the admin panel"""
    list_display = (
        'user',
        'content',
        'created_on'
    )
    list_filter = ('created_on',)