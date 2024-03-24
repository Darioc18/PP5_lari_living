"""Custom template tags for rendering newsletter-related forms."""

from django import template
from newsletter.forms import SubscibersForm

register = template.Library()

@register.inclusion_tag('newsletter/subscription_form.html')
def render_newsletter_form():
    form = SubscibersForm()
    return {'subscribe_form': form}