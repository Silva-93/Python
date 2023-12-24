from django import forms  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore
from contact.models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = Contact  # Modelo para criação do formulário
        # campos do formulário
        fields = 'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture'

        # widgets = {
        #     'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
        #     'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
        #     'phone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
        #     'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )

        return first_name
