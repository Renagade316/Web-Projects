from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "Login.html")

def createaccount(request):
    return render(request, "CreateAccount.html")
    
