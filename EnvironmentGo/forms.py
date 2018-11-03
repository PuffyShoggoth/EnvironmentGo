from django import forms
from EnvironmentGo.models import Photo
from EnvironmentGo.identifier import identify_image
class ImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', )

    def save(self, commit=True):
        instance = super(ImageForm, self).save(commit=False)
        instance.description = identify_image(instance.image)
        if commit:
            instance.save()
        return instance