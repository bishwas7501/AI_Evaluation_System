from django.shortcuts import render

def welcome(request):
    return render(request, 'welcome.html')

def candidate_auth(request):
    return render(request, 'candidate-auth.html')

def hr_auth(request):
    return render(request, 'hr-auth.html')

def instructions(request):
    return render(request, 'instructions.html')

def interview(request):
    return render(request, 'interview.html')

def admin_page(request):
    return render(request, 'admin.html')