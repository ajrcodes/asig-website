from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .models import Brother


@login_required
def index(request):
    """
    View function for home page of the mystic circle (portal) of brothers ALRIGHT
    Shouts Beep chat & all my beepers out there
    """
    # Generate count of all total brothers
    num_brothers = Brother.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_brothers': num_brothers},
    )

from django.views import generic


class BrotherListView(LoginRequiredMixin, generic.ListView):
    model = Brother
    paginate_by = 2


class BrotherDetailView(LoginRequiredMixin, generic.DetailView):
    model = Brother
