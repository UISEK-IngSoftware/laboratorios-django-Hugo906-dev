from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import redirect, render
from pokedex.forms import PokemonForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    pokemons = Pokemon.objects.all() #Select * from pokedex_pokemon
    trainers = Trainer.objects.all() #Select * from pokedex_trainer
    template = loader.get_template('index.html')
    return render(request, 'index.html', {
        'pokemons': pokemons,
        'trainers': trainers
    })

def pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id) #select * from pokedex_pokemon where id = id
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, id: int):
    trainer = Trainer.objects.get(id=id) #select * from pokedex_trainer where id = id
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))


@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

def edit_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})


@login_required
def delete_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id) #select * from pokedex_pokemon where id = id
    pokemon.delete() #delete from pokedex_pokemon where id = id
    return redirect('pokedex:index')

class CustomLoginView(LoginView):
    template_name = 'login_form.html'