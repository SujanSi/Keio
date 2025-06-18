from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, 'pages/home.html')



@csrf_exempt
def send_consultation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        location = data.get('location')
        country = data.get('country')
        education = data.get('education')
        intake = data.get('intake')
        message = data.get('message')
        
        email_message = f"""
        New Free Consultation Request:

        Name: {name}
        Email: {email}
        Phone Number: {phone}
        Location : {location}
        Country: {country}
        Education: {education}
        Preferred Intake: {intake}

        Message:
        {message}
        """

        send_mail(
            subject=f"Free Consultation Request from {name}",
            message=email_message, 
            from_email='dummy123sdum@gmail.com',  # must match settings.py
            recipient_list=['dummy123sdum@gmail.com'],
            fail_silently=False
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'invalid'}, status=400)
