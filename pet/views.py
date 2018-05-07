from django.shortcuts import render, redirect, get_list_or_404

from pet.models import Pet
from .forms import PetForm, OwnerForm

# Create your views here.

def index(request):
    template_name = 'index.html'
    if request.method == 'POST':
        form_pet = PetForm(request.POST)
        form_owner = OwnerForm(request.POST)

        if form_pet.is_valid():
            pet = Pet(
                name = form_pet['name'].value(),
                type_pet = form_pet['type_pet'].value(),
                age = form_pet['age'].value(),
                owner = form_pet['owner'].value(),
            )
            pet.save()
            return redirect('/pet')

        elif form_owner.is_valid():
            owner = form_owner['owner'].value()
            #TODO pasar el valor de owner a la url /query
    else:
        form_pet = PetForm()
        form_owner = OwnerForm()
    context = {'form_pet': form_pet, 'form_owner': form_owner}
    return render(request, template_name = template_name, context = context)

def query_pet(request, owner):
    pets = get_list_or_404(Pet, owner = owner)
    context = {'pets': pets}
    return render(request, template_name = 'query.html', context = context)

def registered(request, name_owner):
    return render(request, template_name = 'registered.html', context = name_owner)
