from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from .models import Flan
from .forms import ContactFormForm


# Create your views here.
def indice(request):
    if request.user.is_authenticated:
        flans = Flan.objects.all()
    else:
        flans = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {"flans": flans})

def about(request):
    return render(request, 'about.html', {})

def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)    
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = ContactFormForm
    return render(request,"contact.html", {"form": form})

class LoginRequiredMixin (View):

    @method_decorator (login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class Welcome(LoginRequiredMixin, TemplateView):
    template_name = "welcome.html"

