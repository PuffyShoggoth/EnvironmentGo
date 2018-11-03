from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
        'image_list': [{
            'image': x.image,
            'latitude' : x.latitude,
            'longitude' : x.longitude,
            'description': x.description,
            'upload_date' : x.uploaded_at,
            'user' : x.uploaded_by,
            } for x in allimages]
    })