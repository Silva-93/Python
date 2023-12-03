from django import forms  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Modelo para criação do formulário
        fields = 'first_name', 'last_name', 'phone', 'email', 'description', 'category'  # campos do formulário
        
        widgets = {
            'first_name': forms.TextInput(attrs= {'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs= {'placeholder': 'Sobrenome'}),
            'phone': forms.TextInput(attrs= {'placeholder': 'Telefone'}),
            'email': forms.EmailInput(attrs= {'placeholder': 'E-mail'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',  # campo onde será exibido a mensagem de erro
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        return super().clean()
    
    def clean_first_name(self):  # Validando o primeiro campo do formulário
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error('first_name', ValidationError('Nome inválido', code='invalid'))