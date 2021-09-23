from django.db import models
from django.shortcuts import render
from blog.models import Categoria, Post

#Create your views here.
def blog(request):
    posts = Post.objects.all() # importando los post guardados en la tabla de post de la app blog de la DDBB
    return render(request, 'blog.html', {'posts':posts})