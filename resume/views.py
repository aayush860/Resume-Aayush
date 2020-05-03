print ('============================')
from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Projects
from skills.models import Skills
from certificates.models import Certificates
# Create your views here.
def helloworld(request):
    projectx=Projects.objects.all()
    certx=Certificates.objects.all()
    skillx=Skills.objects.all()
    return render(request,'index.html',{'proj':projectx,
                                        'skillxx':skillx, 
                                        'certs':certx})