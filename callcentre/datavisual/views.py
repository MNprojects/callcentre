from django.shortcuts import render
from .models import CallRecord
from .forms import ImportExcelForm

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

def test_flowcell(request):
    c = RequestContext(request, {'other_context':'details here'})
    if request.method == 'POST': # If the form has been submitted...
        form = ImportExcelForm(request.POST,  request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            excel_parser= ExcelParser()
            success, log  = excel_parser.read_excel(request.FILES['file'] )
            if success:
                return redirect(reverse('admin:index') + "pages/flowcell_good/") ## redirects to aliquot page ordered by the most recent
            else:
                errors = '* Problem with flowcell * <br><br>log details below:<br>' + "<br>".join(log)
                c['errors'] = mark_safe(errors)
        else:
            c['errors'] = form.errors 
    else:
        form = ImportExcelForm() # An unbound form
    c['form'] = form
    return render_to_response('sequencing/file_upload.html')