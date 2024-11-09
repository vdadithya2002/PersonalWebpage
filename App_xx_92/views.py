from django.shortcuts import render, redirect
from .models import Study, Project, Hobby

def home(request):
    return render(request, 'App_xx_92/resume.html')

def resume_page(request):
   return render(request, 'App_xx_92/resume.html')

def about_page(request):
    return render(request, 'App_xx_92/about.html')

def contact_submit(request):
    if request.method == 'POST':
        return redirect('resume')