from django.shortcuts import render
from .models import Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_photos(request):
    """
	View function to display all the photos in the database
	"""
    # Get list of all photos
    photo_queries = Photo.objects.all()

    # Setup paginator
    paginator = Paginator(photo_queries, 12)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)

    num_photos = Photo.objects.all().count()

    return render(
        request,
        "photos.html",
        context={
            "photos": objects,
            "is_paginated": True}
    )

# Create your views here.
