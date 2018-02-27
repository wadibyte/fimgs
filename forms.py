from django import forms
from django.forms import modelformset_factory
from .models import Fimg


class ImageModelForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Fimg
        fields = ('image', )


ImageFormSet = modelformset_factory(Fimg, form=ImageModelForm, extra=1)
