from django.shortcuts import render, redirect
from contacto.forms import Formulario_contacto
from django.core.mail import send_mail, EmailMessage #clases para enviar un email.

# Create your views here.
def contacto(request):
    formulario_contacto = Formulario_contacto()

    if request.method == 'POST':
        formulario_contacto = Formulario_contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email = EmailMessage('Mensaje enviado desde app django_web_store', f'El usuario con nombre {nombre}, con la dirección {email} escribe lo siguiente: \n\n {contenido}','', ["leo3.14@hotmail.com"], reply_to=[email]) # reply_to=email -> direccion a donde se pueda contestar este correo enviado
            
            #send_mail('Mensaje enviado desde app django_web_store', "El usuario con nombre  con la dirección  escribe lo siguiente: \n\n ", "", ["leo3.14@hotmail.com"])
            
            #email.send()
            try:
                 email.send()
                 return redirect('/contacto/?valido')

            except:
                 return redirect('/contacto/?novalido')

            

    return render(request, 'contacto.html', {'formulario_contacto':formulario_contacto})