from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):

    return render(request, "home.html")
    # return HttpResponse("home")

def servicios(request):

    #return HttpResponse("servicios")
    return render(request, 'servicios.html')

def tienda(request):

    return render(request, 'tienda.html')

def blog(request):

    return render(request, 'blog.html')

def contacto(request):

    return render(request, 'contacto.html')  