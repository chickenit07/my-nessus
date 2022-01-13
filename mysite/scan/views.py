from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import JsonResponse
import simplejson as json
import os

from .forms import *
import mysite.scan.scanner as scanner
# from .scanner import start_scan

# Create your views here.
class ScanningPage(LoginRequiredMixin, TemplateView):
    template_name = 'scanning_page.html'

    def get(self, request):
        form = ScanningForm()
        scans = Scan.objects.all()
        return render(request, self.template_name,{'form':form, 'scans': scans})    
        
class AjaxScan(LoginRequiredMixin, TemplateView):
    def post(self, request):
        if request.headers['X-Requested-With'] == 'XMLHttpRequest' and request.method == "POST":
            # print('test')
            form = ScanningForm(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                # vuln_list = start_scan(instance.host)
                vuln_list = scanner.main(instance.host)
                instance.vuln_arr = vuln_list
                instance.scan_status = "Completed"
                instance.save()
                # print('done')
                # print(vuln_list)
                # instance.vuln_arr = vuln_list
                # instance.save()
                ser_instance = serializers.serialize('json', [ instance, ])
                # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)
            else: 
            # some form errors occured.
                return JsonResponse({"error": form.errors}, status=400)
        # some error occured
        return JsonResponse({"error": ""}, status=400)