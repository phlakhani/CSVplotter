import pandas as pd
from django.shortcuts import render, redirect
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from .dataprocess import handle_uploaded_file, showresult


# Create your views here.
def home(request):

    return render(request, 'home.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('showresult')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def resultview(request):

    datasets = showresult()

    context= {'totalrecords':datasets['totalrecords'],
              'totalcols':datasets['totalcols'],
              'allcols':datasets['allcols']
              }

    return render(request,'showresult.html', context)