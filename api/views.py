from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from .models import *

# Create your views here.
def index(request):
    return redirect("https://ayush-kushwaha.netlify.app/")

def certificates(request):
    resp1 = Certificates.objects.all()
    datas = [each.as_dict() for each in resp1]

    return JsonResponse(datas, safe=False)
    