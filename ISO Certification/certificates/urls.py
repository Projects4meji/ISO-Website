from django.urls import path
from . import views

urlpatterns = [
    path('', views.certifications, name='certifications'),
    path('<slug:slug>/', views.certificate_detail, name='certificate_detail'),
]
