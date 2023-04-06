from django import forms

from characters.models import Character

class CharacterRegisterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = (
            'name', 'full_name', 'nationality', 'description',
            'occupation', 'first_appearance', 'release_year', 'image'
            )
        
    field_order = [
        'name', 'full_name', 'nationality', 'occupation',
        'first_appearance', 'release_year', 'description',
        'image'
        ]
    
class CharacterUpdateForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = (
            'name', 'full_name', 'nationality', 'description',
            'occupation', 'first_appearance', 'release_year'
        )

    field_order = [
        'name', 'full_name', 'nationality', 'occupation',
        'first_appearance', 'release_year', 'description',
        ]
