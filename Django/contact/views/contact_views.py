from django.shortcuts import render, get_object_or_404, redirect  # type: ignore
from django.db.models import Q  # type: ignore
from contact.models import Contact
from django.http import Http404  # type:ignore

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:50]  # mostra os 50 primeiros contatos

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request, 
        'contact/index.html',
        context,
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |  # or 
            Q(last_name__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(phone__icontains=search_value) 
        )\
        .order_by('-id')[0:50]  # mostra os 50 primeiros contatos

    context = {
        'contacts': contacts,
        'site_title': 'Search - '
    }

    return render(
        request, 
        'contact/index.html',
        context,
    )


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_tilte': site_title
    }

    return render(
        request, 
        'contact/contact.html',
        context,
    )