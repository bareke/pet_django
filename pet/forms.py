from django import forms

# Create your forms

class PetForm(forms.Form):
    name = forms.CharField(label = 'name', max_length = 25)
    race = forms.CharField(label = 'race', max_length = 25)
    age = forms.IntegerField(min_value = 1)
    owner = forms.CharField(label = 'owner', max_length = 25)


class OwnerForm(forms.Form):
    owner_query = forms.CharField(label = 'owner', max_length = 25)
