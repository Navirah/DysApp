#django

from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,FileForm
from .models import File
#from . import main
from .HTRrun import runmodel
from .tts import speechConversion
import os




def home(request):
    saved=False
    if request.method=="POST":
        MyFileForm=FileForm(request.POST,request.FILES)
        if MyFileForm.is_valid():
            files=File()
            files.picture=MyFileForm.cleaned_data["picture"]
            files.save()
            saved=True
            module_dir = os.path.dirname(__file__) 
            file_path=os.path.join(module_dir,'media',files.picture.name)
            #result= main.main()
            result=runmodel(file_path)
            #result=main.test_integration()
            speechConversion()
            
    else:
        MyFileForm=FileForm()
    return render(request, 'home.html',locals())
    
def login(request):
    return render(request,'login.html')
    
def reg(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-login')
    else:
        form = UserRegistrationForm()
    return render(request,'reg.html',{'form':form})

