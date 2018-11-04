import json
import mimetypes

from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from environmentgo.forms import ImageForm
from environmentgo.models import Photo


def home(request):
    return render(request, 'display_map.html', {
        'title': 'Environment Go!'
    })

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.uploaded_by = request.user
            model.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {
        'form': form
    })

def map_image_data(request):
    allimages = Photo.objects.all()
    return render(request, 'display_map.html', {
        'image_list': json.dumps([reverse('image_view', args=[x.id]) for x in allimages]),
        'latitudes' : json.dumps([x.latitude for x in allimages]),
        'longitudes' : json.dumps([x.longitude for x in allimages]),
        'descriptions' : json.dumps([x.description for x in allimages]),
    })

def download(request, id):
    image = Photo.objects.get(id=id).image
    return FileResponse(image, filename=image.name)
