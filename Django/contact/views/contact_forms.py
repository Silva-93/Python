from django.shortcuts import render, get_object_or_404, redirect  # type: ignore
from django.db.models import Q  # type: ignore
from contact.models import Contact
from django.core.paginator import Paginator  # type: ignore


def create(request):
    context = {

    }

    return render(
        request,
        'contact/create.html',
        context
    )