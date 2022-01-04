# Generated by Django 2.1.2 on 2022-01-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('scan_id', models.AutoField(primary_key=True, serialize=False)),
                ('scan_name', models.CharField(max_length=100)),
                ('scan_date', models.DateTimeField(auto_now_add=True)),
                ('scan_status', models.CharField(default='Scanning', editable=False, max_length=100)),
                ('host', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vuln',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vuln_name', models.CharField(max_length=100)),
                ('vuln_info', models.CharField(max_length=1000)),
                ('vuln_severity', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]