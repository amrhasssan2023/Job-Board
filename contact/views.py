from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    info = Info.objects.first()

    if request.method == 'POST':
        subject =request.POST['subject']
        emile = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [emile],
        )


    context = {
        'info' : info, 
    }
    return render(request,'contact/contact.html',context)