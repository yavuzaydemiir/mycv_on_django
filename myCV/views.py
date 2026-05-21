from django.http import HttpResponse
from django.shortcuts import render
from .models import Project, PersonalInfo, Skill, Experience, Education, Service, ContactMessage


def index(request):
    # Veritabanındaki tüm verileri çekiyoruz
    projects = Project.objects.all()
    skills = Skill.objects.order_by('-percentage')
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    services = Service.objects.all()

    # Hakkımda bilgisi tek bir satır olacağı için .first() ile ilk kaydı alıyoruz
    personal_info = PersonalInfo.objects.first()

    # Hepsini HTML sayfasına paketleyip gönderiyoruz
    context = {
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'services': services,
        'personal_info': personal_info,
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            return HttpResponse('OK')
        else:
            return HttpResponse('Lütfen tüm alanları doldurunuz.', status=400)

    personal_info = PersonalInfo.objects.first()
    context = {
        'personal_info': personal_info,
    }
    return render(request, 'contact.html', context)