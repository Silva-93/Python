from django import forms  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Modelo para criação do formulário
        fields = 'first_name', 'last_name', 'phone',  # campos do formulário

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',  # campo onde será exibido a mensagem de erro
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()