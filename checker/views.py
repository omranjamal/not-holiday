from django.shortcuts import render
from .models import Entry
import datetime


# Create your views here.


def index(request):
    gimme_date = datetime.datetime.now().date()
    entry = Entry.objects.filter(date__exact=gimme_date).all()
    context = {"status": entry}

    return render(request, 'index.html', context)
