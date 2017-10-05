from django.shortcuts import render
from django.http import HttpResponse
from .models import Newsletter

# Create your views here.
def newsletter(request):
    letter_queries = Newsletter.objects.all()
    num_letters = Newsletter.objects.all().count()
    context={
    "newsletters": letter_queries,
    }
    # return HttpResponse("<H1>I guess I'm beat</H1>")
    return render(request, "newsletters.html", context)
