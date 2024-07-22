from django.shortcuts import render
from blog.models import Post,Categoria

# from blog.models import Post

def blog (request):
     posteo = Post.objects.all()
     return render(request, 'blog.html', {'posts':posteo})

def table(request):
     poster = Post.objects.all()
     return render(request,'table.html',{'posts':poster})

def filtrar_por_categoria(request,categoria):
     posts = Post.objects.filter(categorias_nombre=categoria)
     categorias = Categoria.objects.all()
     return render(request,'blog.html',{'posts':posts,'categorias': categorias})
