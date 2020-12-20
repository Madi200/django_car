from django.shortcuts import render
from django.views import generic
# Create your views here.

from django.http import HttpResponse
from .models import Report, Transport

from django import template

register = template.Library()

# def index(request):
#     context ={
#         "transport": Transport.objects.all()
#     }
#     temp = Transport.objects.get(id=1)
#     print("TTTTTT", temp.report.latest('created'))
#     return render(request, "reporting/index.html", context)


class VesselListView(generic.ListView):
    model = Transport
    template_name = 'reporting/index.html'
    context_object_name = 'transport'
    paginate_by = 5
