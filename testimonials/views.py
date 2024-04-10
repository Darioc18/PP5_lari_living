from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Testimonial
from .forms import TestimonialForm


class TestimonialListView(ListView):
    """
    View to display a list of testimonials.
    """
    model = Testimonial
    template_name = 'testimonials/testimonial_list.html'
    context_object_name = 'testimonials'


class TestimonialCreateView(LoginRequiredMixin,
                            SuccessMessageMixin,
                            CreateView):
    """
    View to create a new testimonial.
    """
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'testimonials/testimonial_create.html'
    success_url = reverse_lazy('testimonial_list')
    success_message = "Testimonial created successfully."

    def dispatch(self, request, *args, **kwargs):
        """
        Method to check if the user has already submitted a testimonial.
        If yes, redirects the user to the testimonial list page.
        """
        if Testimonial.objects.filter(user=self.request.user).exists():
            messages.warning(
                self.request, "You have already added one testimonial.")
            return redirect('testimonial_list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TestimonialUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                            SuccessMessageMixin, UpdateView):
    """
    View to edit a testimonial.
    """
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'testimonials/testimonial_edit.html'
    success_url = reverse_lazy('testimonial_list')
    success_message = "Testimonial updated successfully."

    def test_func(self):
        """
        Check if the current user is the owner of the testimonial or superuser.
        """
        testimonial = self.get_object()
        return (
            self.request.user or
            self.request.user.is_superuser == testimonial.user)


class TestimonialDeleteView(LoginRequiredMixin,
                            SuccessMessageMixin,
                            DeleteView):
    """
    View to delete a testimonial.
    """
    model = Testimonial
    template_name = 'testimonials/testimonial_confirm_delete.html'
    success_url = reverse_lazy('testimonial_list')
    success_message = "Testimonial deleted successfully."

    def test_func(self):
        """
        Check if the current user is the owner of the testimonial or superuser.
        """
        testimonial = self.get_object()
        return (
            self.request.user or
            self.request.user.is_superuser == testimonial.user)

    def delete(self, request, *args, **kwargs):
        """
        Deletes the testimonial and displays a success message.
        """
        messages.success(self.request, self.success_message)
        return super(TestimonialDeleteView, self).delete(
            request, *args, **kwargs
            )
