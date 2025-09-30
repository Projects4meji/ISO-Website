from django.shortcuts import render, get_object_or_404
from .models import Certificate

def certifications(request):
    certificates = Certificate.objects.filter(is_active=True)
    return render(request, 'certificates/certifications.html', {'certificates': certificates})

def certificate_detail(request, slug):
    certificate = get_object_or_404(Certificate, slug=slug, is_active=True)
    return render(request, 'certificates/certificate_detail.html', {'certificate': certificate})