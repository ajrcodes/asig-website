from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.core import serializers
import csv
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Models
from .models import Brother

# Forms
from .forms import SearchBrothersForm


@login_required
def portal(request):
    """
    View function for home page of the mystic circle (portal) of brothers ALRIGHT
    Shouts Beep chat & all my beepers out there
    """
    # Generate count of all total brothers
    num_brothers = Brother.objects.all().count()
    num_alumni = Brother.objects.filter(year="Alumni").count()
    num_actives = Brother.objects.exclude(year="Alumni").count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'brothersportal/index.html',
        context={'num_brothers': num_brothers,
                 'num_alumni': num_alumni,
                 'num_actives': num_actives},
    )


@login_required
def search_form(request):
    """
    View function to handle the search form inputs
    """
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = SearchBrothersForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            """
            View function to handle displaying search results
            """
            # Set up lists to filter the results and get the parameters
            search_results = Brother.objects.all()
            search_parameters = []

            if form.data['first_name']:
                search_parameters.append(form.data['first_name'])
                search_results = list(filter(lambda x: x in search_results,
                                             Brother.objects.filter(first_name=form.data['first_name'])))

            if form.data['last_name']:
                search_parameters.append(form.data['last_name'])
                search_results = list(filter(lambda x: x in search_results,
                                             Brother.objects.filter(last_name=form.data['last_name'])))
            if form.data['year']:
                search_parameters.append(form.data['year'])
                search_results = list(filter(lambda x: x in search_results,
                                             Brother.objects.filter(year=form.data['year'])))
            if form.data['grad_year']:
                search_parameters.append(form.data['grad_year'])
                search_results = list(filter(lambda x: x in search_results,
                                             Brother.objects.filter(grad_year=form.data['grad_year'])))
            if form.data['pledge_class']:
                search_parameters.append(form.data['pledge_class'])
                search_results = list(filter(lambda x: x in search_results,
                                             Brother.objects.filter(pledge_class=form.data['pledge_class'])))
            if form.data['major']:
                search_parameters.append(form.data['major'])
                search_results = list(filter(lambda x: x in search_results,
                                             Brother.objects.filter(major=form.data['major'])))
            if form.data['company']:
                search_parameters.append(form.data['company'])
                search_results = list(filter(lambda x: x in search_results,
                                             Brother.objects.filter(first_name=form.data['last_name'])))
            if form.data['city']:
                search_parameters.append(form.data['city'])
                search_results = list(filter(lambda x: x in search_results,
                                             Brother.objects.filter(first_name=form.data['last_name'])))
            if form.data['state']:
                search_parameters.append(form.data['state'])
                search_results = list(filter(lambda x: x in search_results,
                                             Brother.objects.filter(first_name=form.data['last_name'])))

            # Store results in a session by serializing it
            request.session['search_results'] = serializers.serialize("json", search_results)
            request.session['search_parameters'] = search_parameters

            return HttpResponseRedirect(reverse('search-results'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = SearchBrothersForm()

        return render(
            request,
            'brothersportal/brother_search.html',
            {'form': form}
        )


@login_required
def searchresults(request):
    """
     View function to display all results from a search.  
     NOTE:  Was playing around with the serializers, not sure how to properly cache the results 
            to prevent double queries (from retrieving objects based on pk).  
            Figure this pup out in the future.. works for now.
    """
    # Get list of all brothers
    brothers_list = []
    for obj in serializers.deserialize("json", request.session['search_results']):
        pk = obj.object.pk
        brothers_list.append(Brother.objects.get(pk=pk))
    search_parameters = ', '.join(request.session['search_parameters'])

    # Setup paginator
    paginator = Paginator(brothers_list, 12)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)

    # render template with proper list and parameters
    return render(
        request,
        'brothersportal/brother_list.html',
        context={"brother_list": objects,
                 "search_parameters": search_parameters,
                 "is_paginated": True}
    )


@login_required
def all_brothers(request):
    """
    View function to display all the brothers in the database
    """
    # Get list of all brothers
    brothers_list = Brother.objects.all()

    # Store results in a session by serializing it
    request.session['search_results'] = serializers.serialize("json", brothers_list)

    # Setup paginator
    paginator = Paginator(brothers_list, 12)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)

    # render template with proper list and parameters
    return render(
        request,
        'brothersportal/brother_list.html',
        context={"brother_list": objects,
                 "search_parameters": "All brothers",
                 "is_paginated": True}
    )


@login_required
def all_alumni(request):
    """
    View function to display all the alumni in the database
    """
    # Get list of alumni
    alumni_list = Brother.objects.filter(year="Alumni")

    # Store results in a session by serializing it
    request.session['search_results'] = serializers.serialize("json", alumni_list)

    # Setup paginator
    paginator = Paginator(alumni_list, 12)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)

    # render template with proper list and parameters
    return render(
        request,
        'brothersportal/brother_list.html',
        context={"brother_list": objects,
                 "search_parameters": "All alumni",
                 "is_paginated": True}
    )


@login_required
def all_actives(request):
    """
    View function to display all the actives in the database
    """
    # Get list of actives
    actives_list = Brother.objects.exclude(year="Alumni")

    # Store results in a session by serializing it
    request.session['search_results'] = serializers.serialize("json", actives_list)

    # Setup paginator
    paginator = Paginator(actives_list, 12)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)

    # render template with proper list and parameters
    return render(
        request,
        'brothersportal/brother_list.html',
        context={"brother_list": objects,
                 "search_parameters": "All actives",
                 "is_paginated": True}
    )


@login_required
def export_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="results.csv"'

    writer = csv.writer(response)
    writer.writerow(['First name', 'Last name', 'Email address'])

    # Get list of objects to export
    brothers_list = []
    for obj in serializers.deserialize("json", request.session['search_results']):
        pk = obj.object.pk
        brothers_list.append(Brother.objects.values_list('first_name', 'last_name', 'email').get(pk=pk))

    # do something else with the list if you want

    for obj in brothers_list:
        writer.writerow(obj)

    return response


class BrotherListView(LoginRequiredMixin, generic.ListView):
    model = Brother
    paginate_by = 12


class BrotherDetailView(LoginRequiredMixin, generic.DetailView):
    model = Brother
