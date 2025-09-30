from django.contrib import admin
from .models import Certificate, CertificationStep

class CertificationStepInline(admin.TabularInline):
    model = CertificationStep
    extra = 1
    fields = ['title', 'description', 'icon', 'order']
    ordering = ['order']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description', 'subtitle']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [CertificationStepInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'subtitle', 'icon', 'is_active')
        }),
        ('Content', {
            'fields': ('overview', 'benefits', 'objectives', 'outcomes', 'assessments')
        }),
        ('Images', {
            'fields': ('image_overview', 'image_benefits')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(CertificationStep)
class CertificationStepAdmin(admin.ModelAdmin):
    list_display = ['title', 'certificate', 'order']
    list_filter = ['certificate']
    search_fields = ['title', 'description']
    ordering = ['certificate', 'order']
