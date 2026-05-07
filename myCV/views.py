from django.shortcuts import render
from .models import Project # Modeli içeri aktardık

def index(request):
    projects = Project.objects.all() # Tüm projeleri veritabanından çektik
    return render(request, 'index.html', {'projects': projects}) # Verileri sayfaya gönderdik

def contact(request):
    return render(request, 'contact.html')