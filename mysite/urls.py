from django.contrib import admin
from django.urls import path, include

from mysite.core import views as core_view
from mysite.scan import views as scan_view
from mysite.report import views as report_view

urlpatterns = [
    path('', core_view.home, name='home'),
    path('signup/', core_view.signup, name='signup'),
    path('scanning/', scan_view.ScanningPage.as_view(), name='scanning'),
    path('post/ajax/scan', scan_view.AjaxScan.as_view(), name='ajax_scan'),
    path('report/', core_view.ReportPage.as_view(), name='report'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]