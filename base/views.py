from django.shortcuts import render, redirect, get_object_or_404
from .models import Patients
from .forms import PatientsForm

# Create your views here.

def display(request):
    patients = Patients.objects.all()
    return render(request, 'display.html', {'patients': patients})

def add(request):
    if request.method == 'POST':
        form = PatientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')  # Redirect to a page displaying the list of Patients
    else:
        form = PatientsForm()
    return render(request, 'add.html', {'form': form})


def update(request, pk):
    patient = get_object_or_404(Patients, pk=pk)
    if request.method == 'POST':
        form = PatientsForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('display')  # Redirect to the student list page after updating
    else:
        form = PatientsForm(instance=patient)
    return render(request, 'update.html', {'form': form})

def delete(request, pk):
    patient = get_object_or_404(Patients, pk=pk)
    if request.method == 'POST':
        patient.delete()
    return redirect('display') 



