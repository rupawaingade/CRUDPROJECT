from django.shortcuts import render,HttpResponseRedirect
from .forms import Studentform
from .models import Student
# Create your views here.
def add_show(request):
    if request.method =='POST':

        reg=Studentform(request.POST)
        if reg.is_valid():
            #if we want clean data and then save then we use:
            nm=reg.cleaned_data['name']
            em=reg.cleaned_data['email']
            pw=reg.cleaned_data['password']
            fm =Student(name=nm,email=em,password=pw)
            fm.save()
            reg=Studentform()

    else:
        reg=Studentform()
    stud=Student.objects.all()
        
    return render(request,'enroll/addAndShow.html',{'form':reg,'stu':stud})

#this function is for delete

def delete_data(request,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == "POST":
        up=Student.objects.get(pk=id)
        fm=Studentform(request.POST,instance=up)
        print(fm)
        if fm.is_valid:
            fm.save()
    else:
            up=Student.objects.get(pk=id)
            fm=Studentform(instance=up)
    return render(request,'enroll/updatestudent.html',{'form':fm})