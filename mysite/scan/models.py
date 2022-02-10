from django.db import models


# from django_mysql.models import ListCharField

# Create your models here.

class Vuln(models.Model):
    vuln_id = models.AutoField(primary_key=True,unique=True)
    vuln_name = models.CharField(max_length=100)
    vuln_info = models.CharField(max_length=1000)
    vuln_severity = models.CharField(max_length=100,null = True, blank = True)

    
    def __str__(self):
        return self.vuln_name


class Scan(models.Model):
    scan_id = models.AutoField(primary_key=True)
    scan_name = models. CharField(max_length=100)
    scan_date = models.DateTimeField(auto_now_add=True)
    scan_status = models.CharField(max_length=100, default="Scanning", editable=False)
    host = models.CharField(max_length=100)
    # vuln_list = ArrayField(models.CharField(max_length=100), editable=False)
    # vuln_list = ListCharField(models.CharField(max_length=100), default="", editable=False)
    vuln_list = models.TextField(null=True, editable=False)
    
    # user_id = models.IntegerField()
    # user_id
    # vuln_id = models.ForeignKey(Vuln, default=0, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.scan_name