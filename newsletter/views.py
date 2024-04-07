from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import SubscibersForm, MailMessageForm
from .models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django_pandas.io import read_frame
from django.conf import settings

# Create your views here.

def newsletter(request):
    """View for displaying the newsletter form"""
    template = 'newsletter/newsletter_admin.html'
    form = MailMessageForm()
    return render(request, template)

def subscribe_form(request):
    """View for handling subscription form submission"""
    if request.method == 'POST':
        subscribe_form = SubscibersForm(request.POST)
        if subscribe_form.is_valid():
            email = subscribe_form.cleaned_data.get('email')
            if Subscribers.objects.filter(email=email).exists():
                messages.warning(request, 'You are already subscribed.')
                return redirect(reverse('home'))
            else:
                subscribe_form.save()
                messages.success(request, 'Subscription Successful')
                return redirect(reverse('home'))  # Redirect after form submission
            
    else:
        subscribe_form = SubscibersForm()
    
    context = {
        'subscribe_form': subscribe_form,
    }
    return render(request, 'home/index.html', context)

@login_required
def mail_letter(request):
    """View for sending newsletters to subscribers"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()

    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            email = EmailMessage(
                title,
                message,
                settings.EMAIL_HOST_USER,
                [],  # empty recipient list (email addresses are added to BCC)
                mail_list,  # add the mailing list to BCC
            )
            email.send(fail_silently=False)
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('/')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter_admin.html', context)