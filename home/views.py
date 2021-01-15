from django.shortcuts import render,HttpResponse
from home.models import Contact


# Create your views here.
def home(request):
    #return HttpResponse("this is my homepage")
    context={'name':'ayush','course':'Django'}
    return render(request,'home.html',context)
def about(request):
    var=Contact.objects.all()
    #print(ins)
    #print(data)
    #return HttpResponse("this is my about")
    return render(request,'about.html',{'var':var})
def contact(request):
    ins=Contact.objects.all()
    #print(ins)
    if request.method=="POST":
        #print("this is post")
        fname=request.POST['inputfname']
        lname=request.POST['inputlname']
        email=request.POST['email']
        ph=request.POST['ph']
        ad=request.POST['inputAddress']
        print(fname,lname,email,ph,ad)
        ins=Contact(fname=fname,lname=lname,email=email,ph=ph,ad=ad)
        ins.save()
        print("data is stored in db")
    #return HttpResponse("this is my contact")
    return render(request,'contact.html')

def project(request):
    #return HttpResponse("this is my project")
    return render(request,'project.html')

    