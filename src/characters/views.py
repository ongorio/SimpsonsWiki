from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse, reverse_lazy

from characters.forms import CharacterRegisterForm, CharacterUpdateForm
from characters.models import Character


class CharacterListView(generic.ListView):
    template_name = 'characters.html'
    context_object_name = 'characters'
    model = Character


class CharacterDetailView(generic.DetailView):
    template_name = 'character.html'
    context_object_name = 'character'
    model = Character


class CharacterCreateView(generic.CreateView):
    template_name = 'character_register.html'
    form_class = CharacterRegisterForm
    model = Character


    def get_success_url(self, slug) -> str:

        return reverse('characters:character_detail', kwargs={'slug': slug})

    def form_valid(self, form):
        character = form.save()

        return redirect(self.get_success_url(character.slug))


class CharacterUpdateView(generic.UpdateView):
    template_name = 'character_update.html'
    form_class = CharacterUpdateForm
    context_object_name = 'character'
    model = Character

    def get_success_url(self, slug) -> str:
        return reverse('characters:character_detail', kwargs={'slug': slug})


    def form_valid(self, form):
        character = form.save()

        return redirect(self.get_success_url(character.slug))


class CharacterDeleteView(generic.DeleteView):
    template_name = 'character_confirm_delete.html'
    model = Character
    context_object_name = 'character'
    success_url = reverse_lazy('characters:character_list')