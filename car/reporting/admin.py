from django.contrib import admin

# Register your models here.
from .models import Transport, Report

admin.site.register(Transport)
admin.site.register(Report)
