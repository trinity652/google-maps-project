from django.shortcuts import render
from PIL import Image
from django.core.files.base import ContentFile
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from .models import Record
from .forms import RecordForm
from django.contrib.contenttypes.models import ContentType
from geopy.geocoders import Nominatim

#add for DRF API to work
from rest_framework import generics
from .serializers import RecordSerializer

geolocator = Nominatim()

import requests
#View to see all points
def record_map(request):
	 
	return render(request, "home.html")
  
#create a new location
def create_record(request):
	form = RecordForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		#get coordinates
		location = geolocator.geocode(instance.location)
		instance.latitude = location.latitude
		instance.longitude = location.longitude
		'''
		api_key = ""
		url = "https://maps.googleapis.com/maps/api/staticmap?"
		zoom = 10
		r = requests.get(url + "center =" + str(instance.latitude) +","+str(instance.longitude)+"&zoom =" +str(zoom) + "&size = 400x400&key =" +api_key + "&sensor = false&size=600x400") 
		im = Image.open(r.content)
		im.thumbnail((220, 130), Image.ANTIALIAS)
		thumb_io = BytesIO()
		im.save(thumb_io, im.format, quality=60)
		instance.map_img.save(im.filename, ContentFile(thumb_io.get_value()), save=False)
		'''
		instance.save()
		return HttpResponseRedirect('/')

	context = {  
        "form":form
	}

	return render(request, "app1/create.html", context)

#API to get all records
class RecordAPIView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Record.objects.all()
    serializer_class = RecordSerializer