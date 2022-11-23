from django.shortcuts import render
from django.core.mail import send_mail


def inicio(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')

        context = {
            'nombres': nombres,
            'telefono': telefono,
            'correo': correo,
            'mensaje': mensaje
        }
        cuerpo = '''
            Nombre: {}

            Teléfono: {}

            Mensaje: {}

            Correo: {}

        '''.format(context['nombres'], context['telefono'], context['mensaje'], context['correo'])

        send_mail(context['nombres'], cuerpo, '', ['adsi2374477@gmail.com'])


    return render(request, 'index.html')


def pagina_404(request, exception):
    return render(request, '404.html')




        

    


