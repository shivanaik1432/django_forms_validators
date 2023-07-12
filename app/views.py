from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *

# Create your views here.
def studentform(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFM=Student.objects.get_or_create(name=SFD.cleaned_data['name'],age=SFD.cleaned_data['age'],
            mail=SFD.cleaned_data['mail'],remail=SFD.cleaned_data['remail'],number=SFD.cleaned_data['number'])[0]
            SFM.save()
        else:
            return HttpResponse('Data not valid')
    return render(request,'studentform.html',d)