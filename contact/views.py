from django.shortcuts import render
from .forms import ContactForm
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/contacted.html',{})
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})