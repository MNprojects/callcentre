from django.shortcuts import render
from .models import CallRecord
from .forms import DocumentForm
from django.shortcuts import redirect
from .ExcelParser import ExcelParser

def index(request):
    """
    View function for home page of site.
    """
    allRecords = CallRecord.objects.all()

    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'allRecords':allRecords},
    )




def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            ExcelParser.read_excel(request.FILES['file'])
            return redirect('index')

    else:
        form = DocumentForm()
    return render(request, 'datavisual/model_form_upload.html', {
        'form': form
    })