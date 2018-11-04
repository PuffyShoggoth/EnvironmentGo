from django import forms
from environmentgo.models import Photo
from environmentgo.identifier import identify_image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'latitude', 'longitude')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitude'].widget = forms.HiddenInput()
        self.fields['longitude'].widget = forms.HiddenInput()

    def save(self, commit=True):
        instance = super(ImageForm, self).save(commit=False)
        instance.description = identify_image(instance.image.open(mode='r').read())
        if commit:
            instance.save()
        return instance
