from django.shortcuts import render, redirect, get_list_or_404

from pet.models import Pet
from .forms import PetForm, OwnerForm

# Create your views here.

def index(request):
    template_name = 'index.html'
    if request.method == 'POST':
        form_pet = PetForm(request.POST)
        form_owner = OwnerForm(request.POST)
        print(request.POST, type(request.POST))
        if form_pet.is_valid():
            if 'owner_query' in request.POST:
                print('hey there')
            else:
                print('new pet')
                pet = Pet(
                    name=request.POST['name'][2:-2],
                    race=request.POST['race'][2:-2],
                    age=request.POST['age'][2:-2],
                    owner=request.POST['owner'][2:-2],
                )
                pet.save()
                return redirect('/pet')
        elif form_owner.is_valid():
            context = query_pet(request, request.POST['owner_query'][2:-2])
            context['form_owner'] = form_owner
            context['form_pet'] = form_pet
            template_name = 'query.html'
    else:
        form_pet = PetForm()
        form_owner = OwnerForm()
        print('im here jackass')
        context = {'form_pet': form_pet, 'form_owner': form_owner}
    return render(request, template_name = template_name, context = context)

def query_pet(request, owner):
    pets = get_list_or_404(Pet, owner = owner)
    context = {'pets': pets}
    print('pets are: ', pets)
    return context
    # return render(request, template_name = 'query.html', context = context)

def registered(request, name_owner):
    return render(request, template_name = 'registered.html', context = name_owner)
