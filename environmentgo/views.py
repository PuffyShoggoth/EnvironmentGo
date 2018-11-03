from environmentgo.forms import ImageForm
from django.shortcuts import render, redirect
from environmentgo.models import Photo
from django.http import JsonResponse

def home(request):
    return render(request, 'display_map.html', {
        'title': 'HTTPSAlarm'
    })

def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {
        'form': form
    })

def map_image_data(request):
    allimages = Photo.objects.all()
    return render(request, 'display_map.html', {
        'image_list': [{
            'image': x.image,
            'latitude' : x.latitude,
            'longitude' : x.longitude,
            'description': x.description,
            'upload_date' : x.uploaded_at,
            'user' : x.uploaded_by,
            } for x in allimages]
    })