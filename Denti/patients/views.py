from django.shortcuts import render, get_object_or_404
from .models import Patient

# Create your views here.


def index(request):
    next_patients_list = Patient.objects.order_by("next_treatment")[:10]
    context = {"next_patients_list": next_patients_list}
    return render(request, "patients/index.html", context)


def detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, "patients/detail.html", {"patient": patient})

def birthdays(request, )
