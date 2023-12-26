from django import forms  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm  # type: ignore
from django.contrib.auth.models import User  # type: ignore



class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(attrs={'accept': 'image/*'}))

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


class RegisterForm(UserCreationForm):
    # Tornando campos obrigatórios
    first_name = forms.CharField(required=True, min_length=3)
    last_name = forms.CharField(required=True, min_length=3)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2')

    # Validação do campo de e-mail
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',  # Campo onde será mostrada a msg de erro
                ValidationError('E-mail já existe!')  # Msg que será mostrada.
            )

        return email
