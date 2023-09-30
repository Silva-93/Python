from django.shortcuts import get_object_or_404, render  # type: ignore
from contact.models import Contact

# Create your views here.
def index(request):
    #  Selecionando todos os contatos onde o show for igual a "True"
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')[:10]

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )

#########

def contact(request, contact_id):
    #  selecionando um único valor pela chave primária 
    # single_contact = Contact.objects.get(pk=contact_id).first()

    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )