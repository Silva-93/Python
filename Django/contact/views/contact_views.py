from django.shortcuts import render, get_object_or_404  # type: ignore
from contact.models import Contact
from django.http import Http404  # type:ignore

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:50]  # mostra os 50 primeiros contatos

    context = {
        'contacts': contacts
    }

    return render(
        request, 
        'contact/index.html',
        context,
    )


def contact(request, contact_id):
    single_contacts = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'contact': single_contacts
    }

    return render(
        request, 
        'contact/contact.html',
        context,
    )