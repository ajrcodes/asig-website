from django.shortcuts import render
from .models import Photo

def all_photos(request):
	photo_queries = Photo.objects.all()
	num_photos = Photo.objects.all().count()
	context={
	"photos": photo_queries,
	}
	return render(request, "photos.html", context)

# Create your views here.
