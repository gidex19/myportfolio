from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from myportfolio.settings import BASE_DIR as bdir
import os
import mimetypes


# Create your views here.


def home(request):
    form = ContactForm()

    # C:\Users\this pc\Documents\django_projects\myportfolio\my_app\static\my_app
    return render(request, 'my_app/home.html', {'form': form})


def download(request):
    fp = bdir + "\my_app\static\my_app\ozuluoha-gideons-resume.pdf"

    filename = "gideon-resume.pdf"
    print(fp)
    print(type(bdir))
    fl = open(fp, 'r')
    print("111111111111111111111")
    mime_type, _ = mimetypes.guess_type(fp)
    print(mime_type)
    print("22222222222222222222222222222222222222222")
    response = HttpResponse(fl, content_type=mime_type)
    print("33333333333333333333333333333333333333")
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
