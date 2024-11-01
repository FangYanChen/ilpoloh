from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
      article = Articles.objects.order_by('-id')[:1]
      return render(request, 'main/index2.html', {'article': article})

def about(request):
      return HttpResponse("<h4>iliaz loh</h4>")