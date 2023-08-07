from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *

class Trainer_list(ListView):
    model= Trainer

    template_name='Trainer_list.html'

    context_object_name='tl'
    
    ordering=['trainer_name']

#username=mihir password=mihir