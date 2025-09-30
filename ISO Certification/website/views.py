from django.shortcuts import render, get_object_or_404
from .models import Certificate

# Main app views
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def construction_ehs(request):
    return render(request, 'main/construction_ehs.html')

# Certificate app views
def certifications(request):
    certificates = Certificate.objects.filter(is_active=True)
    return render(request, 'certificates/certifications.html', {'certificates': certificates})

def certificate_detail(request, slug):
    certificate = get_object_or_404(Certificate, slug=slug, is_active=True)
    return render(request, 'certificates/certificate_detail.html', {'certificate': certificate})
