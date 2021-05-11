from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *
from django.http import HttpResponse
from django.core.files.storage import  FileSystemStorage
import random


def home(request):  
    return render(request,"index.html",)
def about_us(request):  
    return render(request,"about.html",)
def contact_us(request):  
    return render(request,"contact.html",)

def apply(request):
    num=random.randrange(1121,9899)
    global str_num
    str_num=str(num)    
    return render(request,"apply.html", {"cap":str_num})


def apply_submit(request):
    
        name= request.POST['Name']
        email_id= request.POST['Email_id']
        years_of_experience=request.POST['Years_of_Experience']
        linkedin_profile= request.POST['Linkedin_Profile']
        expected_hourly_rate=request.POST['Expected_hourly_rate']
        resume= request.FILES['Resume']
        cap=request.POST.get("captha")

        fs=FileSystemStorage()
        fs.save(resume.name, resume)
        Cand = Candidate(Name=name,Email_id=email_id,Years_of_Experience=years_of_experience,Linkedin_Profile=linkedin_profile,
                    Expected_hourly_rate=expected_hourly_rate, Resume= resume,)  
        Cand.save()
        if str(cap)==str_num :
            return HttpResponse("<h4>YOUR APPLICATION HAS BEEN SUBMITED SUCCESSFULLY</h4>")
        else:
            return HttpResponse("<h4>Error captha</h4>")  
        return render(request, "apply.html",)
def jobs(request):
    job_list= Job.objects.all()
    context={'jobs':job_list}
    return render(request,'jobs.html',context=context)    
#def jobs_details(request):
#    job_des= Job.objects.all()
#    context={'jobs_details': job_des}
#    return render(request,'jobs_details.html',context=context)
def jobs_details(request,id):
   
    job_list_1=get_object_or_404(Job,pk=id)
    
    return render(request,'jobs_details.html',{'jobs_1':job_list_1})


