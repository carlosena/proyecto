from django.http import HttpResponse 
from django.shortcuts import render
from django.core.mail import send_mail


# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('full-name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         data = {
#             'name': name,
#             'email': email,
#             'subject': subject,
#             'message': message
#         }
#         message = '''
#         New message: {}

#         From:  {}    

#         '''.format(data['message'], data['email'])
#         send_mail(data['subject'], message, '', ['adsi2374477@gmail.com'])
#         return HttpResponse('Thank you for submitting the form, we will be in touch soon')
#     return render(request, 'inicio/inicio.html')
    