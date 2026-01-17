from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list.html', {'contacts' : contacts})

# def contact_add

# def contact_delete

# def contact_edit

# def contact_search