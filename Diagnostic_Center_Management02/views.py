from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render

def Index(request):
    return render(request, 'App_Blog/index.html')