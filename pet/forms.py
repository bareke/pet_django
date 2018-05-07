from django import forms

# Create your forms

class PetForm(forms.Form):
    name = forms.CharField(label = 'name', max_length = 25)
    type_pet = forms.CharField(label = 'type_pet', max_length = 25)
    age = forms.IntegerField(min_value = 1)
    owner = forms.CharField(label = 'owner', max_length = 25)

class OwnerForm(forms.Form):
    owner = forms.CharField(label = 'owner', max_length = 25)
