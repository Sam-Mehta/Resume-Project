from django.shortcuts import render
from .models import Profile

# Create your views here.
def resume_view(request):
    profile = Profile.objects.first()
    return render(request,'resume/resume.html', {'profile',profile})