from django.shortcuts import render

# Create your views here.
def home_ser(request):

    return render(request, 'home_serv.html')