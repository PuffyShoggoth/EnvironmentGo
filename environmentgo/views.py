from environmentgo.forms import ImageForm
from django.shortcuts import render, redirect


def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
