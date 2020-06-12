from django.forms import ModelForm, forms
from .models import UserLocation, RegiProfile, PlusPhoto
from address.forms import AddressField

class PersonForm(forms.Form):
  address = AddressField()


class LocationForm(ModelForm):
    class Meta:
        model = UserLocation
        fields= ('ispermit',)


class ProfileCreationForm(ModelForm):
    class Meta:
        model = RegiProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['pet_name'].widget.attrs.update({
            'class':"hello",
            'placeholder':'ex)김태훈'
        })


class PlusPhotoForm(ModelForm):
    class Meta:
        model = PlusPhoto
        fields = ('plus_image',)