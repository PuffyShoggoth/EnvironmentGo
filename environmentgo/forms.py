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
        identify_res = identify_image(instance.image.open(mode='r').read())
        instance.description = identify_res[0]
        instance.invasive = identify_res[1]
        if commit:
            instance.save()
        return instance
