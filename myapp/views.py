from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if address and subject and message:
            try:
                # Split addresses into a list
                recipient_list = address.split()  # Split on spaces
                send_mail(
                    subject=subject,  # Use form input
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=recipient_list,  # Use the split addresses
                )
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "index.html", context)
