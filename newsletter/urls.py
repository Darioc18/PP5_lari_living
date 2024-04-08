from django.urls import path
from . import views

urlpatterns = [
    path('subscribe_form/', views.subscribe_form, name='subscribers'),
    path('mail_letter/', views.mail_letter, name='mail_letter')
]
