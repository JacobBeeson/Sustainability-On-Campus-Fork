from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, "ekozumi_app/loginPage.html")

def register(request):
    return render(request, "ekozumi_app/signUpPage.html")