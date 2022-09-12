# la vista 
# render sirve para leer un archivo y devolverlo al cliente
from django.shortcuts import render
import random

# debemos importar httpresponse para mostrar el texto que se devuelve de la clase about, si no lo hacemos nos saldra un error, esto es para devolver un texto sin embargo no queremos devolver solo texto, si no tambien html
# from django.http import HttpResponse
# Create your views here.
# el parametro request es para recibir la informacion del cliente de lo que se esta pidiendo
def home(request):
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('Hello World!!!')
    return render(request, 'about.html')

def password(request):

    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generate_password = ""

    var = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    
    if request.GET.get('simbol'):
        characters.extend(list('!"#$%&/()=?¡+*{-}.'))
    
    if request.GET.get('number'):
        characters.extend(list('123456789'))

    for x in range(var):
        generate_password += random.choice(characters)

    return render(request, 'password.html', {'password': generate_password})