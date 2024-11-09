from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.resume_page, name='resume'),
    path('about/', views.about_page, name='about'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
]