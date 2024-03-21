from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import FormView

class ContactView(FormView):
    """
    View for displaying the contact form and handling form submissions.
    """
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        """
        Handles form submission when it's valid.
        Saves the form data to the database and sends an email notification.
        """
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        # Saving to database
        form.save()

        # Sending email
        send_mail(
            subject,
            f"From: {name}\nEmail: {email}\n\n{message}",
            email,  # User's email as sender
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return super().form_valid(form)

class ContactSuccessView(View):
    """
    View for displaying a success message after the contact form is submitted.
    """
    def get(self, request):
        return render(request, 'contact/contact_success.html')