from django.shortcuts import render

# Create your views here.


def index(request):
    """
    View function for home page of the site.
    """

    # We mapped r'^' to include('core.urls'), the core/templates/index.html file is being used
    return render(
        request,
        'index.html',
    )

def ZYChapterHistory(request):
	return render(request, 'about/ZYChapterHistory.html')

def NationalsHistory(request):
	return render(request, 'about/NationalsHistory.html')

def CurrentLeadership(request):
	return render(request, 'about/CurrentLeadership.html')

def AlumniUpdate(request):
	return render(request, 'alumniupdate.html')

def SupportPage(request):
	return render(request, 'support.html')

def ContactPage(request):
	return render(request, 'contact.html')
