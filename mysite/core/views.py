from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import xml.dom.minidom

from .forms import *
from .exploits import *

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

class ScanningPage(LoginRequiredMixin, TemplateView):
    template_name = 'scanning_page.html'

    def get(self, request):
        form = ScanningForm()
        return render(request, self.template_name,{'form':form})

    def post(self, request):
        form = ScanningForm(request.POST)

        if form.is_valid():
            #get ip addr from brower
            ip_addr = form.cleaned_data['post']
           
            #scanning
            scan_vsftpd_234_backdoor(ip_addr)

            args = {'form': form,'ip_addr': ip_addr}
            return render(request, self.template_name,{'form':form},args)            
        else:
            return render(request,self.template_name,{'form':form})

class ReportPage(LoginRequiredMixin, TemplateView):
    template_name = 'report_page.html'

    # def get(self, request):
    #     form = 