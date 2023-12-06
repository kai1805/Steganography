from django.shortcuts import render
from django.http import HttpResponse, request
import mimetypes
from django.core.files.storage import FileSystemStorage
import os
from . import steg
import asyncio
import json


def index(request):    
    context = {}
    if request.method == "POST":        
        if request.POST['demoMode'] == 'encode':
            uploaded_file = request.FILES['image'] 
            fs = FileSystemStorage()        
            file = fs.save(uploaded_file.name, uploaded_file) 
            text = request.POST['demoText']          
            print(file)
            file_res = steg.steganography(file, text)
            context['url'] = fs.url(file_res)    

        elif request.POST['demoMode'] == 'decode':            
            uploaded_file = request.FILES['image']            
            fs = FileSystemStorage()        
            file = fs.save(uploaded_file.name, uploaded_file)
            stegano_res = steg.steganography_decode(file)
            context['decode'] = stegano_res        
    return render(request, 'pages/base.html', context)


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'core/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'pages/base.html')
    

# def download_file():
#      # fill these variables with real values
#     fl_path = '/media/'
#     filename = ''
#     request.GET['f']

#     fl = open(fl_path, 'r')
#     mime_type, _ = mimetypes.guess_type(fl_path)
#     response = HttpResponse(fl, content_type=mime_type)
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     return response

# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'core/model_form_upload.html', {
#         'form': form
#     })
