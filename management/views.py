from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import copy,random
import math
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
import nexmo


def Home(request):
    context={}
    return render(request,'management/home.html',context)


def Entry(request):
    if request.POST:
        if "otp" in request.POST:
            if str(request.POST["otp"]) == str(request.session["otp"]):
                host=Host.objects.filter(name=request.session["country"])
                for h in host:
                    host=h
                e=EntryModel.objects.create(host=host,name=request.session["name"],email=request.session["email"],phone=request.session["phone"],Description=request.session["subject"])
                print("send entry sms")

                mail_subject = 'Visitor Details'
                message = "Name : " + str(request.session["name"]) + "\nphone no. : " + str(request.session["phone"]) + "\nPurpose of visit : " + str(request.session["subject"]) + "\n\n Dear " + str(host.name) + ", visitor is about to meet you."
                to_email = str(host.Email)
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                        )
                email.send()

                client = nexmo.Client(key='5a3f9685', secret='umP5sNVyOLg4TFRP')
                client.send_message({
                    'from': '+917013250001',
                    'to': '+91' + str(request.session["phone"]),
                    'text': message,
                })

                context={}
                return render(request,'management/home.html',context)
            # print(request.session["otp"])
            context={"mail":request.session["email"],"phone":request.session["phone"],"msg":"*You have entered worng OTP. Please try again."}
            return render(request,'management/otp.html',context)
        request.session["name"]=request.POST['fname']+" "+request.POST['lname']
        request.session["email"]=request.POST['email']
        request.session["phone"]=request.POST['phone']
        request.session["host"]=request.POST['host']
        request.session["subject"]=request.POST['subject']
        request.session["otp"]=random.randint(1000,9999)

        mail_subject = 'OTP.'
        message = "Your 4 letter OTP :" + str(request.session["otp"])
        to_email = request.session["email"]
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
        email.send()

        print("mail,sms",request.session["otp"])
        context={"mail":request.session["email"],"phone":request.session["phone"],"msg":""}
        return render(request,'management/otp.html',context)
    h=Host.objects.all()
    context={"hosts":h}
    return render(request,'management/entry.html',context)





def Exit(request):
    if request.POST:
        if "otp" in request.POST:
            if str(request.POST["otp"]) == str(request.session["otp"]):
                entry=EntryModel.objects.filter(name=request.session["ename"])
                for e in entry:
                    entry=e
                host= entry.host
                print("Out sms and email")
                new=ExitModel.objects.create(host=entry.host,name=entry.name,email=entry.email,phone=entry.phone,Description=entry.Description,checkin=entry.checkin)
                print(new)

                mail_subject = 'Visitor Log'
                message = "Visitor Name : " + str(request.session["name"]) + "\nHost Name : " + str(entry.host) + "\nVisitor Phone no. : " + str(request.session["phone"]) + "\nPurpose of visit : " + str(request.session["subject"]) + "\nEntry Time : " + str(entry.checkin) + "\nExit time : " + str(entry.checkin)
                to_email = str(host.Email)
                email = EmailMessage(
                            mail_subject, message, to=[to_email,str(entry.email)]
                        )
                email.send()

                client = nexmo.Client(key='5a3f9685', secret='umP5sNVyOLg4TFRP')
                client.send_message({
                    'from': '+917013250001',
                    'to': '+91' + str(entry.phone),
                    'text': message,
                })
                client.send_message({
                    'from': '+917013250001',
                    'to': '+91' + str(host.ph ),
                    'text': message,
                })

                EntryModel.objects.filter(name=request.session["ename"]).delete()
                context={}
                return render(request,'management/home.html',context)
            else:
                entry=EntryModel.objects.filter(name=request.session["ename"])
                for e in entry:
                    entry=e
                print(request.session["otp"])
                context={"mail":entry.email,"phone":entry.phone,"msg":"*You have entered worng OTP. Please try again."}
                return render(request,'management/otp.html',context)
        request.session["ename"]=request.POST['name']
        request.session["otp"]=random.randint(1000,9999)
        print("mail,sms",request.session["otp"])
        entry=EntryModel.objects.filter(name=request.session["ename"])
        for e in entry:
            entry=e

        mail_subject = 'OTP.'
        message = "Your 4 letter OTP :" + str(request.session["otp"])
        to_email = str(entry.email)
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
        email.send()

        context={"mail":entry.email,"phone":entry.phone,"msg":""}
        return render(request,'management/otp.html',context)
    e=EntryModel.objects.all()
    context={"exit":e}
    return render(request,'management/exit.html',context)
