from django.urls import path
from . import views

urlpatterns = [
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonial_list'),
    path('create/', views.TestimonialCreateView.as_view(), name='testimonial_create'),
    path('<int:pk>/edit/', views.TestimonialUpdateView.as_view(), name='testimonial_edit'),
    path('<int:pk>/delete/', views.TestimonialDeleteView.as_view(), name='testimonial_confirm_delete'),
]