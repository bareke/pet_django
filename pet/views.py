from django.shortcuts import render, redirect, get_list_or_404

from pet.models import Pet
from .forms import PetForm, OwnerForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form_pet = PetForm(request.POST)
        print(request.POST, type(request.POST), request.POST['owner'], type(request.POST['owner']))
        form_owner = OwnerForm(request.POST)
        if form_pet.is_valid():
            pet = Pet(
                name=request.POST['name'][2:-2],
                race=request.POST['race'][2:-2],
                age=request.POST['age'][2:-2],
                owner=request.POST['owner'][2:-2],
            )
            pet.save()
            return redirect('/pet')
        elif form_owner.is_valid():
            pass
    else:
        form_pet = PetForm()
        form_owner = OwnerForm()
        context = {'form_pet': form_pet, 'form_owner': form_owner}
    return render(request, template_name = 'index.html', context = context)

def query_pet(request, owner):
    pets = get_list_or_404(Pet, owner = owner)
    context = {'pets': pets}
    return render(request, template_name = 'query.html', context = context)

def registered(request, name_owner):
    return render(request, template_name = 'registered.html', context = name_owner)
