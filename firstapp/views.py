from django.shortcuts import render, redirect, reverse
from firstapp.parsing import *
from .models import DataAfterParsing


def firstview(request):
    data = DataAfterParsing.objects.all()
    return render(request, 'firstapp/face_of_pars.html', context={'name': data})


def pars_button(request):
    parsing_url(request)
    return redirect(reverse(firstview))
