from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
   context = {
            'posts': Post.objects.all(),
            'user': request.user
   }
   return render(request, 'tekeza/index.html', context)

def about(request):
   return render(request, 'tekeza/about.html')