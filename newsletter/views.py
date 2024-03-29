from django.shortcuts import render, redirect, reverse
from .forms import SubscibersForm, MailMessageForm
from .models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame

# Create your views here.

def newsletter(request):
    """Subscribers page view"""
    template = 'newsletter/newsletter_admin.html'
    form = MailMessageForm()
    return render(request, template)

def subscribe_form(request):
    if request.method == 'POST':
        subscribe_form = SubscibersForm(request.POST)
        if subscribe_form.is_valid():
            email = subscribe_form.cleaned_data.get('email')
            if Subscribers.objects.filter(email=email).exists():
                messages.warning(request, 'You are already subscribed.')
            else:
                subscribe_form.save()
                messages.success(request, 'Subscription Successful')
                return redirect(reverse('home'))  # Redirect after form submission
            
    else:
        subscribe_form = SubscibersForm()
    
    context = {
        'subscribe_form': subscribe_form,
    }
    return render(request, 'home\index.html', context)


def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('/')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter_admin.html', context)