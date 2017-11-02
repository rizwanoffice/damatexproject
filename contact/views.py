from django.shortcuts import render
from damatex_overseas_app.models import CarousalImages
from .forms import ContactForm
# Create your views here.


def contact(request):
    carosual_images = CarousalImages.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/contacted.html',{'carosual_images': carosual_images})
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form, 'carosual_images': carosual_images})