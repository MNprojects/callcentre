from django.shortcuts import render

# Create your views here.


from .models import CallRecord

def index(request):
    """
    View function for home page of site.
    """

    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={},
    )