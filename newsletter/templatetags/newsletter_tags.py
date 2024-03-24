from django import template
from newsletter.forms import SubscibersForm  # Adjust the import path as needed

register = template.Library()

@register.inclusion_tag('newsletter/subscription_form.html')
def render_newsletter_form():
    form = SubscibersForm()
    return {'subscribe_form': form}