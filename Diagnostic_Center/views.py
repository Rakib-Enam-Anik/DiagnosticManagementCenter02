from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate, logout, login


# Create your views here.

def About(request):
    return render(request, 'Diagnostic_Center/about.html')


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('index')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'Diagnostic_Center/view_doctor.html', d)

def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('index')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['specialization']
        try:
            Doctor.objects.create(name=n, mobile=c, specialization=sp)
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'Diagnostic_Center/add_doctor.html', d)

def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('index')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('Diagnostic_Center/view_doctor.html')

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('index')
    pat = Patient.objects.all()
    d = {'pat': pat}
    return render(request, 'Diagnostic_Center/view_patient.html', d)

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('index')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['age']
        add = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, age=a, address=add)
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'Diagnostic_Center/add_patient.html', d)

def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('index')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('Diagnostic_Center/view_patient.html')

def View_Technician(request):
    if not request.user.is_staff:
        return redirect('index')
    tec = Technician.objects.all()
    d = {'tec': tec}
    return render(request, 'Diagnostic_Center/view_technician.html', d)

def Add_Technician(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        try:
            Technician.objects.create(name=n, gender=g, mobile=m)
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'Diagnostic_Center/add_technician.html', d)

def Delete_Technician(request, pid):
    if not request.user.is_staff:
        return redirect('index')
    technician = Technician.objects.get(id=pid)
    technician.delete()
    return redirect('Diagnostic_Center/view_technician.html')
    

