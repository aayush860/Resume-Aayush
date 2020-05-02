print ('============================')
from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Projects
# Create your views here.
def helloworld(request):
    projectx=Projects.objects.all()
    
    return render(request,'index.html',{'proj':projectx})