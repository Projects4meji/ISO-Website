from django.db import models
from django.urls import reverse

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    subtitle = models.CharField(max_length=200, blank=True, help_text="Subtitle for the certificate")
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    overview = models.TextField(help_text="Overview points separated by newlines")
    benefits = models.TextField(help_text="Benefits points separated by newlines")
    objectives = models.TextField(blank=True, help_text="Learning objectives separated by newlines")
    outcomes = models.TextField(blank=True, help_text="Learning outcomes separated by newlines")
    assessments = models.TextField(blank=True, help_text="Assessment methods separated by newlines")
    image_overview = models.ImageField(upload_to='certificates/', blank=True, null=True)
    image_benefits = models.ImageField(upload_to='certificates/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('certificate_detail', kwargs={'slug': self.slug})

    def get_overview_list(self):
        return [point.strip() for point in self.overview.split('\n') if point.strip()]

    def get_benefits_list(self):
        return [point.strip() for point in self.benefits.split('\n') if point.strip()]
    
    def get_objectives_list(self):
        return [point.strip() for point in self.objectives.split('\n') if point.strip()]
    
    def get_outcomes_list(self):
        return [point.strip() for point in self.outcomes.split('\n') if point.strip()]
    
    def get_assessments_list(self):
        return [point.strip() for point in self.assessments.split('\n') if point.strip()]

class CertificationStep(models.Model):
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, related_name='steps')
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.certificate.name} - {self.title}"
