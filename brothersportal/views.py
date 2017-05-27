from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
    num_actives = Brother.objects.filter(year= not "Alumni").count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'brothersportal/index.html',
        context={'num_brothers': num_brothers,
                 'num_alumni': num_alumni,
                 'num_actives': num_actives},
    )


@login_required
def search_brothers(request):
    """
    View function for searching the brothersportal
    """
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = SearchBrothersForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
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

            # Pass in filtered list of brothers and list of parameters
            search_parameters = ', '.join(search_parameters)
            return render(
                request,
                'brothersportal/brother_list.html',
                context={"brother_list": search_results,
                         "search_parameters": search_parameters}
            )

    # If this is a GET (or any other method) create the default form.
    else:
        form = SearchBrothersForm()

    return render(
        request,
        'brothersportal/brother_search.html',
        {'form': form}
    )


@login_required
def all_brothers(request):
    """
    View function to display all the brothers in the database
    """
    # Get list of alumni
    brothers_list = Brother.objects.all()
    # render template with proper list and parameters
    return render(
        request,
        'brothersportal/brother_list.html',
        context={"brother_list": brothers_list,
                 "search_parameters": "All brothers"}
    )


@login_required
def all_alumni(request):
    """
    View function to display all the alumni in the database
    """
    # Get list of alumni
    alumni_list = Brother.objects.filter(year="Alumni")
    # render template with proper list and parameters
    return render(
        request,
        'brothersportal/brother_list.html',
        context={"brother_list": alumni_list,
                 "search_parameters": "All alumni"}
    )


@login_required
def all_actives(request):
    """
    View function to display all the actives in the database
    """
    # Get list of alumni
    actives_list = Brother.objects.filter(y)
    # render template with proper list and parameters
    return render(
        request,
        'brothersportal/brother_list.html',
        context={"brother_list": actives_list,
                 "search_parameters": "All actives"}
    )


class BrotherListView(LoginRequiredMixin, generic.ListView):
    model = Brother
    paginate_by = 12


class BrotherDetailView(LoginRequiredMixin, generic.DetailView):
    model = Brother
