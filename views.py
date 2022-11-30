from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import weighttrack
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

class signup(CreateView):
    form_class= UserCreationForm
    template_name='templates/register.html'
    success_url='/weighttrack/weight'

class logoutauth(LogoutView):
    template_name="templates/weightlogout.html"

class loginauth(LoginView):
    template_name="templates/weightlogin.html"

class weightListView(ListView):
    model= weighttrack
    context_object_name="wieghts"
    template_name= "templates/weightlist.html"

class weightCreateView(CreateView):
    model= weighttrack
    fields=['title','text']
    success_url='/weighttrack/weight'

class weightDetailView(DetailView):
    model= weighttrack
    context_object_name="wieghts"
    template_name= "templates/weightdetails.html"

def say_hello(request):
    return render(request, 'hello.html', {'name':'anshul'}, {'today': datetime.today()})

def list(request):
    all_weight=weighttrack.objects.all()
    return render(request, 'wieghttrack/templates/weightlist.html', {'weights': all_weight})

def details(request, pk):
    weight=weighttrack.objects.get(pk=pk)
    return render(request, 'wieghttrack/templates/weightdetails.html', {'weights': weight})

@login_required
def authorized(request):
    return render(request, 'authorized.html', {} )
