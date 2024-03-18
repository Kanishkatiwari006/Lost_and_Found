from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from firstApp.models import lost
from firstApp.models import found
from firstApp.models import contacts
from django.conf import settings
from django.contrib import messages
import requests
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,"home.html")

def get_in_touch(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        messages=request.POST.get("message")
        if User.objects.filter(email = email).exists():
            if contacts.objects.filter(Name=name, Email = email,Phone = phone,Message=messages).exists():
                return render(request,'home.html')
            else:
                k=contacts(Name=name,Email=email,Phone=phone,Message=messages)
                k.save()
                return redirect(home)
        else:
              return redirect(home)       
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        email=request.POST.get("em","default")
        name=request.POST.get("name","default")
        password=request.POST.get("Pw","default") 
        if User.objects.filter(email = email).exists():
                messages.info(request,"Email already exists....")
                return redirect(register)
        else:
                user=User.objects.create_user(first_name=name,email=email,password=password,username=email)
                user.save()
                return redirect(login) 
    return render(request,"register.html")

def login(request):
    if request.method == "POST":
        username=request.POST.get("username","default")
        password=request.POST.get("Pw")  
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            messages.info(request,"Invalid Credentials....")
            return redirect(login)
    return render(request,"login.html")

def after_login(request):
    return render(request,"after_login.html")

def products(request):
    return render(request,"products.html")

def Lost(request):
    return render(request,"products.html")

def Found(request):
     return render(request,"after_found.html")


def after_found(request):
    if request.method == "POST":
         product=request.POST.get("options","default")
         others=request.POST.get("ot")
         addr=request.POST.get("place", "default")
         pin=request.POST.get("pin")
         email=request.POST.get("em")
         ques= request.POST.get("ques")
         x=found(Product=product,Other=others,Address=addr,Pin=pin,Email=email,Ques=ques)
         x.save()
         messages.info(request,"Your data has been saved....")
         return redirect(after_found) 
    return render(request,"after_found.html")

def item(request):
     return render(request,"item.html")

def after_products(request):
    if request.method == "POST":
         product=request.POST.get("options","default")
         others=request.POST.get("ot")
         pin=request.POST.get("pin")
         y=found.objects.filter(Product=product,Pin=pin).values()
         return render(request,"item.html",{'y': y})
    return render(request, 'after_products.html')

def claim(request):
     if request.method == 'POST':
          Id=request.POST.get("id")
          y=list(found.objects.filter(id=Id).values())
          product=y[0]['Product']
          pin=y[0]['Pin']
          que=y[0]['Ques']
          ques=request.POST.get("que")
          addr=request.POST.get("place", "default")
          info=request.POST.get("mark")
          num=request.POST.get("num")
          image= request.POST.get("image")
          if lost.objects.filter(Product=product,Pin=pin,Ques=ques,Address=addr,Info=info,Num=num).exists():
             messages.info(request,"Data already exists....")
             return redirect(item)
          else:
            subject='LOST THING'
            message=f'Query for your found item \n\n Item = {product},\n\n Pin = {pin},\n\n {que} \n {ques},\n\n Address = {addr},\n\n Info = {info},\n\n Contact No. = {num},\n\n Image = {image}'
            from_email=settings.EMAIL_HOST_USER
            recipient_list= [y[0]['Email']]
            send_mail(subject, message, from_email, recipient_list)
            x=lost(Product=product,Address=addr,Pin=pin,Ques=ques,Info=info,Num=num,Image=image)
            x.save()
            messages.info(request,"Your Query is recorded.The founder will contact you soon. Thankyou....")
            return redirect(item)
     return render(request,"item.html")

def logout(request):
     auth.logout(request)
     return redirect(home)