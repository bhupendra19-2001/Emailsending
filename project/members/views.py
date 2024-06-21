from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response

class Sendmail(APIView):
    def post(self,request):
        email=request.data['to']
        emailw=EmailMessage(
            'Email From SMTP Server',
            'This Email From Bhupendra Kekti side..',
            settings.EMAIL_HOST_USER,
            [email]
        )

        # Provide the correct file path to attach_file method
        # For example, emailw.attach_file('/path/to/your/file.txt')
        # Replace '/path/to/your/file.txt' with the actual path to your file
        emailw.attach_file('a.jpg')

        emailw.send(fail_silently=False)
        return Response({'status':True,'message':'Email sent successfully'})
