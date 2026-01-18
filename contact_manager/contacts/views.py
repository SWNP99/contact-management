from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list.html', {'contacts' : contacts})

def contact_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact.objects.create(name=name, email=email, phone=phone)
        return render(request, 'contacts/partials/contact_row.html', {'contact' : contact})
    return HttpResponse(status=400)

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return HttpResponse('')


def contact_edit(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == "POST":
        contact.name = request.POST["name"]
        contact.email = request.POST["email"]
        contact.phone = request.POST["phone"]
        contact.save()

        return render(request, "contacts/partials/contact_row.html", {
            "contact": contact
        })

    return render(request, "contacts/partials/contact_edit_form.html", {
        "contact": contact
    })


def contact_search(request):
    query = request.GET.get("q", "")
    contacts = Contact.objects.filter(name__icontains=query)

    return render(request, "contacts/partials/contact_rows.html", {
        "contacts": contacts
    })
