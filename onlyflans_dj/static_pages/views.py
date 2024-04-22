from django.shortcuts import render
from django import forms
from .models import Flan, ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ContactFormForm

# Create your views here.
def indice(request):
    flanes = Flan.objects.all()
    flanes_pub = Flan.objects.filter(is_private=False)
    flanes_priv = Flan.objects.filter(is_private=True)
    return render(request, 'index.html', {"flanes_pub": flanes_pub})

def about(request):
    return render(request, 'about.html', {})

def welcome(request):
    return render(request, 'welcome.html', {})

def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)    
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = ContactFormForm
    return render(request,"contact.html", {"form": form})

